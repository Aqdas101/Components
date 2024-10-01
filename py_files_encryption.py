# place all python files path in python_files


from cryptography.fernet import Fernet
import glob

key = b'c9PGl7mpWfZDOCo67ZymRG_mCFZmifdFusN1E5nXs0o='
cipher = Fernet(key)

# python_files = glob.glob("*.py")
python_files = ["/content/image_to_text.py"]
print(python_files)

for file_name in python_files:
  print(file_name)

  with open(file_name, 'rb') as file:
      encrypted_code = cipher.encrypt(file.read())

  with open(file_name[:-3]+'.enc', 'wb') as file:
      file.write(encrypted_code)
