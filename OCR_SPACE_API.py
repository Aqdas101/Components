from PIL import Image
import requests
import io

def image_to_text(image: Image.Image) -> str:
  img_byte_arr = io.BytesIO()
  image.save(img_byte_arr, format='PNG')
  img_byte_arr.seek(0)


  api_key = "YOUR_API_KEY"
  url = 'https://api.ocr.space/parse/image'

  # Prepare the files and payload
  files = {
      'filename': ('image.png', img_byte_arr, 'image/png')
  }
  data = {
      'apikey': api_key,
      'language': 'eng'  # Specify language if needed
  }

  # Send the request
  response = requests.post(url, files=files, data=data)
  json_ = response.json()

  if json_['OCRExitCode'] != 1:
    raise Exception('The OCR Space API request failed')
  else:
      text = json_['ParsedResults'][0]['ParsedText']

  return text
