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
input = ['v1.mp4','v2.mp4','v3.mp4','v4.mp4','v5.mp4','v6.mp4']
output = ['v1o.mp4','v2o.mp4','v3o.mp4','v4o.mp4','v5o.mp4','v6o.mp4']

for i in range(6):
    remove_audio(input[i], output[i])
