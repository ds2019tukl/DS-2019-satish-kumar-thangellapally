import unittest
import pandas as pd


def get_minimum(d1):
    return d1.min()


def get_maximum(d1):
    return d1.max()


def get_avg(d1):
    return d1.mean()


class TestTimeMethods(unittest.TestCase):
    def test_get_minimum(self):
        d = {'col1': [1, 0, 2, 9, 8, 5], 'col2': [10, 0, -1, 1, -4, 6]}
        d1 = pd.DataFrame(data=d)
        self.assertEqual(get_minimum(d1["col1"]), 0)
        self.assertEqual(get_minimum(d1["col2"]), -4)

    def test_get_avg(self):
        d = {'col1': [1, 2, 3, 4, 5], 'col2': [10, 0, -1, 1, -4]}
        d1 = pd.DataFrame(data=d)
        self.assertEqual(get_avg(d1["col1"]), 3)
        self.assertEqual(get_avg(d1["col1"]), 3)

    def test_get_maximum(self):
        d = {'col1': [1, 0, 2, 9, 8, 5], 'col2': [10, 0, -1, 1, -4, 6]}
        d1 = pd.DataFrame(data=d)
        self.assertEqual(get_maximum(d1["col1"]), 9)
        self.assertEqual(get_maximum(d1["col2"]), 10)


if __name__ == '__main__':
    unittest.main()







