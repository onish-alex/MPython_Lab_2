from dieselEngine import DieselEngine
from internalCombustionEngine import InternalCombustionEngine
from jetEngine import JetEngine
from random import randint

def makeEngineArray(count):
    array = []
    for i in range(count):
        type_num = randint(1, 3)
        if (type_num == 1):
            array.append(DieselEngine(randint(1, 100), randint(1, 100)))
        elif (type_num == 2):
            array.append(InternalCombustionEngine(randint(1, 100), randint(1, 100)))
        else: 
            array.append(JetEngine(randint(1, 100), randint(1, 100)))
    return array

def main():
    engines = makeEngineArray(10)
    for i in engines:
        i.doWork()

main()
