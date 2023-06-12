from car import Car
from tyres.carrigan_tyres import CarriganTyres
from tyres.octoprime_tyres import OctoprimeTyres
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

class CarFactory:
    def __init__(self):
        pass
    def create_calliope(self,current_date,last_service_Date,current_mileage,last_service_mileage,tyre_wear):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=SpindlerBattery(current_date,last_service_Date)
        tyres=CarriganTyres(tyre_wear)
        return Car(engine,battery,tyres)
    
    def create_glissade(self,current_date,last_service_Date,current_mileage,last_service_mileage,tyre_wear):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=NubbinBattery(current_date,last_service_Date)
        tyres=OctoprimeTyres(tyre_wear)
        return Car(engine,battery,tyres)
    
    def create_palindrome(self,current_date,last_service_Date,warning_light_on,tyre_wear):
        engine=SternmanEngine(warning_light_on)
        battery=SpindlerBattery(current_date,last_service_Date)
        tyres=CarriganTyres(tyre_wear)
        return Car(engine,battery,tyres)
    
    def create_rorschach(self,current_date,last_service_Date,current_mileage,last_service_mileage,tyre_wear):
        engine=WilloughbyEngine(current_mileage,last_service_mileage)
        battery=NubbinBattery(current_date,last_service_Date)
        tyres=OctoprimeTyres(tyre_wear)
        return Car(engine,battery,  tyres)
    
    def create_thovex(self,current_date,last_service_Date,current_mileage,last_service_mileage,tyre_wear):
        engine=CapuletEngine(current_mileage,last_service_mileage)
        battery=NubbinBattery(current_date,last_service_Date)
        tyres=CarriganTyres(tyre_wear)
        return Car(engine,battery)

