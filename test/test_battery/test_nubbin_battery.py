import unittest
from datetime import date,datetime

from battery.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service(self):
        today = date.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today,last_service_date)
        self.assertTrue(battery.needs_service())
    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-01-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())