import unittest
from salary_calculation import calculate_salary


class EquivalencePartitioning(unittest.TestCase):

    def test_manager_invalid(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=-1), -1)

    def test_manager_underwork(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=25), 2500)

    def test_manager_normal(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=40), 4000)

    def test_manager_overwork(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=45), 5000)

    def test_employee_invalid(self):
        self.assertEqual(calculate_salary(is_manager=False, working_hours=-1), -1)

    def test_employee_underwork(self):
        self.assertEqual(calculate_salary(is_manager=False, working_hours=25), 3000)

    def test_employee_normal(self):
        self.assertEqual(calculate_salary(is_manager=False, working_hours=40), 3000)

    def test_employee_overwork(self):
        self.assertEqual(calculate_salary(is_manager=False, working_hours=45), 3000)


if __name__ == '__main__':
    unittest.main()