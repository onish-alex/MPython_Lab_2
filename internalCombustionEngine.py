from engine import Engine

class InternalCombustionEngine(Engine):
    def __init__(self, power, petrol_consumption):
        Engine.__init__(self, power)
        self.petrol_consumption = petrol_consumption
    def doWork(self):
        super().doWork()
        print("...and eats {} litres of petrol!".format(self.petrol_consumption))
        