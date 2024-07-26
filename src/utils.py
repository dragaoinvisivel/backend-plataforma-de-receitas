import os
from app import  db, Lesson
from video_utils import get_video_duration_v1
from app import db, Course

def list_and_register_lessons(course_path, course_id):
    Lesson.query.filter_by(course_id=course_id).delete()
    list_and_register_lessons_in_directory(course_path, course_id, "")
    db.session.commit()

def list_and_register_lessons_in_directory(directory, course_id, hierarchy_prefix=""):
    entries = list(os.scandir(directory))
    entries.sort(key=lambda e: (e.is_file(), os.path.splitext(e.name)[0]))

    for entry in entries:
        if entry.is_dir():
            new_hierarchy_prefix = f"{hierarchy_prefix}/{entry.name}" if hierarchy_prefix else entry.name
            list_and_register_lessons_in_directory(entry.path, course_id, new_hierarchy_prefix)
        elif entry.is_file() and entry.name.lower().endswith((".mp4", ".avi", ".mov", ".wmv", ".flv", ".mkv", ".webm", ".pdf", ".ts", ".txt", "html")):
            title = os.path.splitext(entry.name)[0]
            is_pdf = entry.name.lower().endswith(".pdf")

            duration = get_video_duration_v1(entry.path)
            
            video_url = "" if is_pdf else entry.path
            pdf_url = entry.path if is_pdf else ""

            lesson = Lesson(
                course_id=course_id,
                title=title,
                module=hierarchy_prefix,
                hierarchy_path=hierarchy_prefix,
                video_url=video_url,
                duration=str(duration),
                progressStatus='not_started',
                isCompleted=0,
                time_elapsed='0',
                pdf_url=pdf_url
            )
            db.session.add(lesson)

    db.session.commit()

def scan_data_directory_and_register_courses():
    entries = list(os.scandir('/data'))

    for entry in entries:
        if entry.is_dir():
            course = Course(
                name=entry.name,
                path=entry.path,
                isCoverUrl=0,
                fileCover=None,
                urlCover=None
            )

            if course_already_exists(course):
                return

            db.session.add(course)
            db.session.commit()

            list_and_register_lessons_in_directory(course.path, course.id)

def course_already_exists(course: Course):
    return bool(len(Course.query.filter(Course.path == course.path).all()))