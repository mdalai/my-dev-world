
'''
  SECRET_KEY="kJotxT6v4AaHCY3wXs8-cCS5CfERtIepsC6aKIz6xVM=" \
    python3 symmetric_client.py
'''

import os
import requests
from cryptography.fernet import Fernet


SECRET_KEY = os.environb[b"SECRET_KEY"]
cipher = Fernet(SECRET_KEY)


def get_secret_message():
    res = requests.get("http://127.0.0.1:5683")
    decrypted_msg = cipher.decrypt(res.content)
    print(f"The code is: {decrypted_msg}")

if __name__ == "__main__":
    get_secret_message()