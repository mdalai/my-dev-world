
'''
  uwsgi --http-socket 127.0.0.1:5683 \
    --env SECRET_KEY="kJotxT6v4AaHCY3wXs8-cCS5CfERtIepsC6aKIz6xVM=" \
    --mount /=symmetric_server:app
'''



from flask import Flask
import os
from cryptography.fernet import Fernet

SECRET_KEY = os.environb[b"SECRET_KEY"]
SECRET_MSG = b"fluffy tail"
app = Flask(__name__)

cipher = Fernet(SECRET_KEY)

@app.route("/")
def get_secret_message():
    return cipher.encrypt(SECRET_MSG)
