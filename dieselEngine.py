from engine import Engine

class DieselEngine(Engine):
    def __init__(self, power, diesel_consumption):
        Engine.__init__(self, power)
        self.diesel_consumption = diesel_consumption
    def doWork(self):
        super().doWork()
        print("...and eats {} litres of diesel fuel!".format(self.diesel_consumption))
        