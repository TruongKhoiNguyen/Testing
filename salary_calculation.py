HOURLY_WAGE = 100
BASE_SALARY = 3000


def calculate_salary(is_manager: bool, working_hours: int) -> int:
    '''
    Calculate salary of an employee based on their position and working hours. Return -1 if input is invalid, otherwise return monthly salary as normal.
    '''
    if working_hours < 0 or working_hours > 168:
        return -1
    
    if is_manager:
        if working_hours <= 40:
            return working_hours * HOURLY_WAGE
        return HOURLY_WAGE * 40 + 2 * HOURLY_WAGE * (working_hours - 40)
    
    return BASE_SALARY