from random import*
from roomDataFunctions import*
import time

while(1):
    T=randint(15,35)
    H=randint(30,90)
    print(T)
    TemperatureTest(T) 
    print(H)
    HumidityTest(H)
    time.sleep(10)
    print("\n")