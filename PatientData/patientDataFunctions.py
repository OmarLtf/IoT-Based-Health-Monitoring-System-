from random import*
import time


def BodyTemperature(temp) : 
    tempval = {
        "minNormalVal" : 36,
        "maxNormalVal" : 37.5, 
    }
    if((temp < tempval["maxNormalVal"])and(temp > tempval["minNormalVal"])) : 
        print("Normal ")
    elif (temp > tempval["maxNormalVal"]) : 
        print("Abnormal Temp (Hight) ")
    elif (temp < tempval["minNormalVal"]) : 
        print("Abnormal Temp (Low)")


def BodyPosition(bodyPos,spesificPos):
   # ascii =[100,108,114,115,117]
   # d=chr(ascii[randint(0,4)])
   if (bodyPos != spesificPos):
       print("Warning! Patient in the wrong position")
   # Waiting for Dash Library
    


def Heartbits(signal,BPM):
    # Waiting for Dash library
    print(signal)
    print(BPM)





