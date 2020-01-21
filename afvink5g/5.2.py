class waggie:

    def __init__(self, __year_model, __make, __speed):
        self.__year_model = __year_model
        self.__make = __make
        self.__speed = __speed


    def accelerate(self):
        self.__speed = int(self.__speed + 10)

    def brake(self):
        self.__speed = int(self.__speed - 10)

    def get_speed(self):
        return self.__speed

Bentley = waggie('2010', 'Bentley', 90)


for y in range(5):
    Bentley.accelerate()
    print(Bentley.get_speed())

for x in range(0, 5):
    Bentley.brake()
    if x == 4:
        print(Bentley.get_speed())

