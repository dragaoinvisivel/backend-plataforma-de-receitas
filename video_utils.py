import subprocess
import re
import subprocess
import os

def get_video_duration_v1(video_path):
    command = ['ffmpeg', '-i', video_path]
    try:
        result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = result.communicate()[0].decode('utf-8')
        duration_match = re.search(r'Duration: (\d+):(\d+):(\d+)', output)
        if duration_match:
            hours, minutes, seconds = map(int, duration_match.groups())
            total_seconds = hours * 3600 + minutes * 60 + seconds
            return total_seconds
        else:
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
    
def open_video(video_path):
    if os.path.exists(video_path):
        print(video_path)
        try:
            os.startfile(video_path)
        except:
            print("erro ao abrir arquivo")
        return 
    
    print("Caminho do vídeo não encontrado.")