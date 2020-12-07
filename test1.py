import unittest
from expenses import my_mean, site_checker
from unittest import mock


class TestMyMean(unittest.TestCase):

    def test_my_mean_int(self):
        self.assertEqual(my_mean([1,]), 1)

    def test_my_mean_list(self):
        self.assertEqual(my_mean([2, 3, 4]), 3)

    def test_my_mean_float(self):
        self.assertEqual(my_mean([1.1, 2.2, 3.3]), 6.6/3)

    def test_my_mean_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            res = my_mean([])

    def test_my_mean_string(self):
        with self.assertRaises(TypeError):
            res = my_mean(['1', 2, 3])


class TestSiteChecker(unittest.TestCase):
    @mock.patch('expenses.get_site_status', return_value=200)
    def test_tut_by(self, mock_get_site_status):
        url = 'https://tut.by'
        self.assertEqual(site_checker(url), f'site { url } is ok.')

    @mock.patch('expenses.get_site_status', return_value='Error')
    def test_tut_byq(self, mock_get_site_status):
        url = 'https://tut.byq'
        self.assertEqual(site_checker(url), f'site { url } is not ok.')
        self.assertIsNone(mock_get_site_status.assert_called_once_with(url)) # try to uncomment line 30 of funcs.py


if __name__ == '__main__':
    unittest.main()