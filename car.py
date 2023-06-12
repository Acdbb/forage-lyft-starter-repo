from servicable import Servicable
class Car(Servicable):
    def __init__(self, engine, battery, tyres):
        self.engine = engine
        self.battery = battery
        self.tyres = tyres

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyres.needs_service()
