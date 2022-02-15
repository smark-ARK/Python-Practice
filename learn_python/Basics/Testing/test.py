import unittest
from city_country import city_country


class Test(unittest.TestCase):
    def test_cico(self):
        destination = city_country("PAK", "Hyd")
        self.assertEqual(destination, "PAK, Hyd")


if __name__ == "__main__":
    unittest.main()
