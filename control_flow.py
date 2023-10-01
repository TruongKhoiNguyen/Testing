import unittest
from salary_calculation import calculate_salary


class ControlFlow(unittest.TestCase):

    def test_invalid(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=-1), -1)
    
    def test_manager_and_underwork(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=25), 2500)
    
    def test_manager_and_overwork(self):
        self.assertEqual(calculate_salary(is_manager=True, working_hours=45), 5000)
    
    def test_employee(self):
        self.assertEqual(calculate_salary(is_manager=False, working_hours=40), 3000)


if __name__ == '__main__':
    unittest.main()