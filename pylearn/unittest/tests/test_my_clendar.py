import unittest
from mypkgs import my_calendar
from mypkgs.my_calendar import requests
from requests.exceptions import Timeout
from unittest.mock import patch


class TestMyClendar(unittest.TestCase):
    @patch('mypkgs.my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
        mock_requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            my_calendar.get_holidays()
            mock_requests.get.assert_called_once()

    @patch.object(requests, 'get', side_effect=requests.exceptions.Timeout)
    def test_get_holidays_timeout2(self, mock_requests):
        with self.assertRaises(requests.exceptions.Timeout):
            my_calendar.get_holidays()


if __name__ == "__main__":
    unittest.main()