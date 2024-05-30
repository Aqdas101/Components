# dependencies
# ! pip install --upgrade -q faster-whisper

# functionality: Take audio path and return transcription


from faster_whisper import WhisperModel

def convert_audio_to_text(audio_file: str):
  model_size = "large-v2"
  model = WhisperModel(model_size, device="cuda", compute_type="float16")
  segments, info = model.transcribe(audio_file, beam_size=1)
  transcription = ''.join([segment.text for segment in segments])
  return transcription

# convert_audio_to_text('audio_path')
