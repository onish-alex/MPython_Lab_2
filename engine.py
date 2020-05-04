class Engine:
    def __init__(self, power):
        self.power = power
    def doWork(self):
        print("It works with {} power!".format(self.power))
    