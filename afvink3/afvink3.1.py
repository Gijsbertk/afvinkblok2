def main():
    vraag = inputt()
    radius, gravity, periode = variabelen()
    verwerk(vraag, radius, gravity, periode)



def inputt():
    vraag = input("Van welke maan van jupiter wil je de statistieken weten?: ")
    return vraag

def variabelen():
    radius = {'Io':1821.6,'Europa':1560.8,'Ganymede':2634.1,'Callisto':2410.3}
    gravity = {'Io':1.796,'Europa':1.314,'Ganymede':1.428,'Callisto':1.235}
    periode = {'Io':1.769,'Europa':3.551,'Ganymede':7.154,'Callisto':16.689}
    return radius, gravity, periode


def verwerk(vraag, radius, gravity, periode):
    print('De maan',vraag,'heeft een radius van',radius[vraag])
    print('De maan',vraag,'heeft een zwaartekracht van',gravity[vraag])
    print('De maan',vraag,'heeft een periode van',periode[vraag])


main()