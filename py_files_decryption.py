from cryptography.fernet import Fernet
import os
import subprocess
import tempfile

# Your secret encryption key
cipher = Fernet("c9PGl7mpWfZDOCo67ZymRG_mCFZmifdFusN1E5nXs0o=")

# Files containing encrypted functions and code
files = ['/content/my_extractor.enc']
decrypted_code = ""

# Decrypt each file and merge the decrypted code
for file in files:
    with open(file, 'rb') as f:
        encrypted_code = f.read()
    decrypted_code += cipher.decrypt(encrypted_code).decode('utf-8') + "\n"
