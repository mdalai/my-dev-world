
#from __future__ import absolute_import

import unittest
import test_utils

import sys_topic_producer


class TestSysTopicProducer(unittest.TestCase):

    def setUp(self):
        self.config_file = 'test_config'
        test_utils.create_config_file(self.config_file)

    def tearDown(self):
        test_utils.delete_config_file(self.config_file)

    def test_get_os(self):
        os = sys_topic_producer.get_os(self.config_file)
        self.assertEqual('Windows 10', os)

    def test_get_sw_ver(self):
        self.assertEqual('Spring Boot 3.11', sys_topic_producer.get_sw_ver(self.config_file))

    def test_get_group(self):
        self.assertEqual('org.group', sys_topic_producer.get_group(self.config_file))


if __name__ == '__main__':
    unittest.main()
