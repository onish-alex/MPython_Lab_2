from engine import Engine

class JetEngine(Engine):
    def __init__(self, power, fuel_consumption):
        Engine.__init__(self, power)
        self.fuel_consumption = fuel_consumption
    def doWork(self):
        super().doWork()
        print("...and eats {} litres of jet fuel!".format(self.fuel_consumption))
        