from lesson_8.task_2 import timeit
from time import sleep
import unittest
import pytest


def function_for_testing(sleep_time):
    """Test function only for testing decorator timeit.

    :param float sleep_time : time in seconds
    """
    sleep(sleep_time)


class TestTimeitDecorator(unittest.TestCase):
    """Test suit for testing decorator timeit"""
    def test_treshold_bad_value(self):
        """Test bad value for treshold parameter."""
        with self.assertRaises(TypeError):
            timeit(threshold='abc')(function_for_testing)()

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        """Capture function's output."""
        self.capsys = capsys

    def test_no_treshold(self):
        """Test return of execution time, no treshold provided."""
        timeit()(function_for_testing)(1)
        captured = self.capsys.readouterr()
        self.assertIn('secs', captured.out)

    def test_treshold_less_than_func_time(self):
        """Test should return execution time"""
        timeit(threshold=0.1)(function_for_testing)(0.3)
        captured = self.capsys.readouterr()
        self.assertIn('secs', captured.out)

    def test_treshold_greater_than_func_time(self):
        """Test should NOT return execution time"""
        timeit(threshold=0.3)(function_for_testing)(0.1)
        captured = self.capsys.readouterr()
        print(captured)
        self.assertNotIn('secs', captured.out)
