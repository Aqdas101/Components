# Dependencies 
# ! pip install pytube pydub

# Funtionality: Get YouTube Video Link and return Video or Audio
  # audio = False -- Return Video

from pytube import YouTube
from pydub import AudioSegment
import os

class YoutubeDownloader:
    def __init__(self, url: str):
        self.url = url

    def download_youtube_video(self, audio: bool = True ):  

      yt = YouTube(self.url)
      video = yt.streams.filter(only_audio=audio).first()
      downloaded_file = video.download()
      
      if audio:
        base, ext = os.path.splitext(downloaded_file)
        mp3_file = base + '.mp3'
        audio = AudioSegment.from_file(downloaded_file)
        audio.export(mp3_file, format='mp3')
        os.remove(downloaded_file)
      else:
        mp3_file = downloaded_file


      print(f"Downloaded and converted to MP3: {mp3_file}")

# dw = YoutubeDownloader('YOUTUBE_VIDEO_URL')
# dw.download_youtube_video(audio=False)
