
# set env var:
# export SECRET_URL=http://127.0.0.1.7683
# or
# SECRET_URL="http://127.0.0.1.7683" python3 client.py

import os 
import requests


def get_secret_message():
    url = os.environ["SECRET_URL"]
    response = requests.get(url)
    print(f"The secret message is: {response.text}")

def get_secret_message_https():
    response = requests.get("https://localhost:5683", verify="ca-public-key.pem")
    print(f"The secret message is: {response.text}")


if __name__ == '__main__':
    get_secret_message()