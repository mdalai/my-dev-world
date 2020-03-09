
#from __future__ import absolute_import

import unittest
import test_utils

import producer_utils


class TestProducerUtils(unittest.TestCase):
    def setUp(self):
        self.config_file = 'test_config'
        test_utils.create_config_file(self.config_file)

    def tearDown(self):
        test_utils.delete_config_file(self.config_file)

    def test_parse_config_file(self):
        expected = {'batch version': 'rls.120', 'GROUP': 'org.group', 'left white space': '5', 'with no right value': '', 'OS': 'Windows 10', 'Software': 'Spring Boot 3.11', 'right white space': '3'}
        observed = producer_utils.parse_config_file(self.config_file)
        self.assertDictEqual(expected, observed)


if __name__ == '__main__':
    unittest.main()
