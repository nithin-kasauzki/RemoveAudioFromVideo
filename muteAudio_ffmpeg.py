# import os
# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

from moviepy.editor import VideoFileClip

def remove_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    video_without_audio = video.set_audio(None)
    video_without_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')
    video.close()
    video_without_audio.close()

# Example usage
input = 'v1.mp4'
output = 'v1o.mp4'

remove_audio(input[i], output[i])
