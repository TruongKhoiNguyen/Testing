import unittest
from salary_calculation import calculate_salary


class DataFlow(unittest.TestCase):

    def test_01(self):
        # test for path 0-1(F)-3(F)-6
        self.assertEqual(calculate_salary(
            is_manager=False, working_hours=40), 3000)

    def test_02(self):
        # test for path 0-1(T)-2
        self.assertEqual(calculate_salary(
            is_manager=False, working_hours=-1), -1)

    def test_03(self):
        # test for path 0-1(F)-3(T)-4(T)-5
        self.assertEqual(calculate_salary(
            is_manager=True, working_hours=40), 4000)

    def test_04(self):
        # test for path 0-1(F)-3(T)-4(F)-7
        self.assertEqual(calculate_salary(
            is_manager=True, working_hours=45), 5000)


if __name__ == '__main__':
    unittest.main()
