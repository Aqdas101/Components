from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_clip(video_path: str, start_time: int, duration: int, output_path: str):
    with VideoFileClip(video_path) as video:
        end_time = start_time + duration
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(output_path, codec='libx264')


extract_clip()
