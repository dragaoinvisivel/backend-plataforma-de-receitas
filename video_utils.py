import subprocess
import re

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