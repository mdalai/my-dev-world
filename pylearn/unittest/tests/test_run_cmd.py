
import unittest

from mypkgs import cmd
from unittest import mock
from unittest.mock import patch
 

class TestRunCommand(unittest.TestCase):


    def test_run_cmd_any(self):
        with self.assertRaises(Exception):
            cmd.run_cmd_return_output('anycmd', args=[])

    @patch('mypkgs.cmd.subprocess.Popen')
    def test_run_cmd_exception(self, mock_subprocess_popen):
        proc_mock = mock.Mock()
        attrs = {'communicate.return_value': ('output', 'error')}
        proc_mock.configure_mock(**attrs)
        mock_subprocess_popen.return_value = proc_mock 
        with self.assertRaises(Exception):
            cmd.run_cmd_return_output('echo', args=[])
        self.assertTrue(mock_subprocess_popen.called)


if __name__ == "__main__":
    unittest.main()
