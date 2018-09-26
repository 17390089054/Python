import unittest
from Employee import Employee
class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee=Employee('Yang','Shlley',2000)
        self.increment=2000
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(5000,self.employee.salary)
    def test_give_custom_raise(self):
        self.employee.give_raise(increment=2000)
        self.assertEqual(7000,self.employee.salary)
unittest.main()       
