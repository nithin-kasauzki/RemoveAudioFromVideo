import cv2

def remove_audio_opencv(input_video_path, output_video_path):
    video_capture = cv2.VideoCapture(input_video_path)
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break
        video_writer.write(frame)

    video_capture.release()
    video_writer.release()

#Example usage
input_video_path = 'v1.mp4'
output_video_path = 'v1o.mp4'

remove_audio_opencv(input_video_path, output_video_path)
