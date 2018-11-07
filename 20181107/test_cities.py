import unittest
from city_functions import get_city_country

class TestCitiesCase(unittest.TestCase):
    def test_city_country(self):
        city = get_city_country('Santiago','Chile')
        self.assertEqual(city,'Santiago Chile')
    def test_city_population(self):
        city = get_city_country('Santiago','Chile',population=5000000)
        self.assertEqual(city,'Santiago, Chile - 5000000')

unittest.main() 