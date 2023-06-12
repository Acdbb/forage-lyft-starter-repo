import unittest

from tyres.octoprime_tyres import OctoprimeTyres
class TestOctoprimeTyres(unittest.TestCase):
    def test_tyres_needs_service(self):
        tyre_wear = [0.9,0.8,0.9,0.9]
        tyres = OctoprimeTyres(tyre_wear)
        self.assertTrue(tyres.needs_service())
    def test_tyres_needs_service_false(self):
        tyre_wear = [0.5,0.4,0.7,0.8]
        tyres = OctoprimeTyres(tyre_wear)
        self.assertFalse(tyres.needs_service())