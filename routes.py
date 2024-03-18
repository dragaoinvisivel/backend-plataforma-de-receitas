
from flask import request, jsonify, send_file, abort, send_from_directory, render_template
from werkzeug.utils import secure_filename
import os
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import joinedload

from app import app, db, Lesson, Course
from utils import list_and_register_lessons
from video_utils import open_video

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/courses', methods=['GET'])
def list_courses():
    courses = Course.query.all()
    return jsonify([{'id': course.id, 'name': course.name, 'path': course.path, 'isCoverUrl': course.isCoverUrl, 'fileCover': course.fileCover, 'urlCover': course.urlCover } for course in courses])

@app.route('/api/courses/<int:course_id>/lessons', methods=['GET'])
def list_lessons_for_course(course_id):
    lessons = Lesson.query \
        .filter_by(course_id=course_id) \
        .options(joinedload(Lesson.course)) \
        .all()

    response = [{
        'course_title': lesson.course.name if lesson.course else None,
        'id': lesson.id,
        'title': lesson.title,
        'module': lesson.module,
        'progressStatus': lesson.progressStatus,
        'isCompleted': lesson.isCompleted,
        'hierarchy_path': lesson.hierarchy_path,
        'time_elapsed': lesson.time_elapsed,
        'video_url': lesson.video_url,
        'duration': lesson.duration,
        'pdf_url': lesson.pdf_url,
    } for lesson in lessons]
    
    return jsonify(response)


@app.route("/serve-content", methods=['GET'])
def serve_lesson_content():
    path = request.args.get('path')
    if '..' in path or path.startswith('/'):
        abort(404)

    if not os.path.exists(path):
        abort(404)
        
    if path.lower().endswith(".ts") or path.lower().endswith(".mkv"):
        open_video(path)
        return send_from_directory("assets", "video-aviso-reproducao.mp4")      

    return send_file(path)

@app.route('/api/update-lesson-progress', methods=['POST'])
def update_lesson_for_end_progress():
    data = request.json
    lesson_id = data.get('lessonId')
    progress_status = data.get('progressStatus')
    is_completed = data.get('isCompleted')
    time_elapsed = data.get('time_elapsed', None)

    lesson = Lesson.query.get(lesson_id)
    if lesson:
        if progress_status:
            lesson.progressStatus = progress_status
        if is_completed is not None:
            lesson.isCompleted = is_completed
        if time_elapsed is not None:
            lesson.time_elapsed = time_elapsed

        db.session.commit()
        return jsonify({'message': 'Progresso da lição atualizado com sucesso'})
    else:
        return jsonify({'error': 'Lição não encontrada'}), 404


@app.route('/api/courses', methods=['POST'])
def add_course():
    name = request.form['name']
    path = request.form['path']
    
    isCoverUrl = 1 if 'imageURL' in request.form and request.form['imageURL'] else 0
    urlCover = request.form.get('imageURL', None)

    if not isCoverUrl:
        image_file = request.files.get('imageFile')
        if image_file:
            filename = secure_filename(image_file.filename)
            fileCover = filename
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            fileCover = None
    else:
        fileCover = None

    course = Course(
        name=name,
        path=path,
        isCoverUrl=isCoverUrl,
        fileCover=fileCover,
        urlCover=urlCover if isCoverUrl else None
    )
    print(f"Saving course with file cover: {course.fileCover}")
    db.session.add(course)
    db.session.commit()

    list_and_register_lessons(request.form['path'], course.id)

    return jsonify({'id': course.id, 'name': course.name}), 201

@app.route('/api/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({'id': course.id, 'name': course.name})

@app.route('/api/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson_elapsed_time(lesson_id):
    lesson = Lesson.query.get_or_404(lesson_id)
    print(lesson.time_elapsed)
    return jsonify({"elapsedTime": lesson.time_elapsed}) 


@app.route('/api/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get_or_404(course_id)
    old_path = course.path
    course.name = request.form['name']
    course.path = request.form['path']
    isCoverUrl = 1 if 'imageURL' in request.form and request.form['imageURL'] else 0

    if isCoverUrl:
        course.urlCover = request.form.get('imageURL')
        course.isCoverUrl = 1
        course.fileCover = None
    else:
        image_file = request.files.get('imageFile')
        if image_file:
            filename = secure_filename(image_file.filename)
            course.fileCover = filename
            course.isCoverUrl = 0
            course.urlCover = None
            image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            course.fileCover = course.fileCover
    print(f"Saving course with file cover: {course.fileCover}")
    db.session.commit()
    if old_path != course.path:
        list_and_register_lessons(course.path, course_id)
    

    return jsonify({'id': course.id, 'name': course.name, 'path': course.path, 'isCoverUrl': course.isCoverUrl, 'fileCover': course.fileCover, 'urlCover': course.urlCover})

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/api/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    print(course)
    print(course_id)
    
    Lesson.query.filter_by(course_id=course_id).delete()
    
    if course.fileCover:
        try:
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], course.fileCover))
        except FileNotFoundError:
            print(f"Arquivo {course.fileCover} não encontrado.")

    db.session.delete(course)
    db.session.commit()
    return jsonify({'message': 'Course and associated lessons deleted'})



@app.route('/api/courses/<int:course_id>/completed_percentage', methods=['GET'])
def course_completion_percentage(course_id):
   
    course = Course.query.get_or_404(course_id)

    if course is None:
        return jsonify({'error': 'Curso não encontrado'}), 404

    total_lessons = len(Lesson.query \
        .filter_by(course_id=course_id) \
        .all())

    if total_lessons == 0:
        return jsonify({'error': 'Curso não tem aulas'}), 400

    completed_lessons = Lesson.query.filter_by(course_id=course_id, isCompleted=1).count()

    completion_percentage = (completed_lessons / total_lessons) * 100

    return jsonify({'completion_percentage': completion_percentage})