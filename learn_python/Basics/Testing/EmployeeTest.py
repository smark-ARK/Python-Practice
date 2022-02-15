import unittest
from Employee import Employee


class EmployeeTest(unittest.TestCase):
    def setUp(self):
        self.E = Employee("Abdul", "Rehman", 10000)

    def test_default_Raise(self):
        self.E.give_raise()
        self.newsald = self.E.get_sal()
        self.assertEqual(15000, self.newsald)

    def test_custom_rais(self):
        self.E.give_raise(200)
        self.newsal = self.E.get_sal()
        self.assertEqual(10200, self.newsal)


if __name__ == "__main__":
    unittest.main()
