
# credit: https://realpython.com/python-mock-library/

from datetime import datetime
import requests


def is_weekday():
    today = datetime.today()
    print(f'===> {today}')
    # monday-0, ..., sunday=6
    return (0 <= today.weekday() < 5)



def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
    

if __name__ == "__main__":
    print(f'Is today weekday? {is_weekday()}')
