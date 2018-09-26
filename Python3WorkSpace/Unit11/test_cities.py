import unittest
from city_functions import get_city
class testcity(unittest.TestCase):
    def test_city_country(self):
        name=get_city('santiago','chile')
        self.assertEqual('Santiago,Chile',name)
    def test_city_country_population(self):
        name=get_city('santiago','chile',population=5000000)
        self.assertEqual('Santiago,Chile - population 5000000',name)
    
unittest.main()
