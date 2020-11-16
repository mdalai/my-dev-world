
# credit: https://realpython.com/python-mock-library/

from datetime import datetime
from unittest.mock import Mock

from requests.exceptions import Timeout
import unittest


# generate test days using actaul datetime
monday = datetime(year=2020, month=11, day=9)
sat = datetime(year=2020, month=11, day=14)


def is_weekday():
    today = datetime.today()
    print(f'===> {today}')
    # monday-0, ..., sunday=6
    return (0 <= today.weekday() < 5)


datetime = Mock() 

# mock today is Monday
datetime.today.return_value = monday
print(datetime.today())
assert is_weekday()
# mock today is Saturday
datetime.today.return_value = sat
print(datetime.today())
assert not is_weekday()


## ---------------------------------------------

requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestMyClendar(unittest.TestCase):
    def log_request(self, url):
        print(f'Making a request to {url}')
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock
    
    def test_get_holidays_logging(self):
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'

    def test_get_holidays_timeout(self):
        # mock connection timeout
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()



if __name__ == "__main__":
    print(f'Is today weekday? {is_weekday()}')
    unittest.main()
