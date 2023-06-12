import unittest

from tyres.carrigan_tyres import CarriganTyres
class TestCarriganTyres(unittest.TestCase):
    def test_tyres_needs_service(self):
        tyre_wear = [0.9,0.8,0.9,0.9]
        tyres = CarriganTyres(tyre_wear)
        self.assertTrue(tyres.needs_service())
    def test_tyres_needs_service_false(self):
        tyre_wear = [0.8,0.8,0.8,0.8]
        tyres = CarriganTyres(tyre_wear)
        self.assertFalse(tyres.needs_service())
