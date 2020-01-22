class pet:
    """worden de variabelen toegekend"""

    def __init__(self, __name, __age, __type):
        self.__name = __name
        self.__age = __age
        self.__type = __type

    """deze functies vragen om de input die ze daarna weer terug geven aan de user"""

    def SetName(self):
        self.__name = input('Geef de naam van je huisdier: ')
    def SetAge(self):
        self.__age = input('Geef de leeftijd van je huisdier: ')
    def SetType(self):
        self.__type = input('Geef de soort van je huisdier: ')
    def GetName(self):
        return self.__name
    def GetAge(self):
        return self.__age
    def GetType(self):
        return self.__type

    """roept de functies aan"""


dier1 = pet('', '', '')
dier1.SetName()
dier1.SetAge()
dier1.SetType()
print(dier1.GetAge(), dier1.GetType(), dier1.GetName())











