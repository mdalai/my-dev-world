

# how to start: uwsgi --http-socket 127.0.0.1:5683 --mount /=server:app


from flask import Flask

SECRET_MSG = "fluffy tail"
app = Flask(__name__)

@app.route("/")
def get_secret_message():
    return SECRET_MSG
