
def TemperatureTest(temp) : 
    tempval = {
        "minNormalVal" : 19,
        "maxNormalVal" : 24, 
    }
    if((temp < tempval["maxNormalVal"])and(temp > tempval["minNormalVal"])) : 
        print("Confort Temperature")
    elif (temp > tempval["maxNormalVal"]) : 
        print("Hot, turn on the air conditioner ")
    elif (temp < tempval["minNormalVal"]) : 
        print("Cold, turn on the air conditioner")


def HumidityTest(hum) : 
    humval = {
        "minNormalVal" : 30,
        "maxNormalVal" : 60
    }
    if((hum < humval["maxNormalVal"])and(hum > humval["minNormalVal"])) : 
        print("Confort Humidity")
    elif (hum > humval["maxNormalVal"]) : 
        print("Humidity excceted the normal, open the windows")
    elif (hum < humval["minNormalVal"]) : 
        print("Humidity under the normal")

        



    