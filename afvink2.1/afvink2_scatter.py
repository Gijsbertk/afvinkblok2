import matplotlib.pyplot as plt
def main():
    een()
    """de main roept de funties aan """

def een():
    patienten_csv = open('patienten.csv','r')
    header = patienten_csv.readline()
    patienten_lijst = list()
    """leest opent bestand en maakt een lijst aan """

    for x in patienten_csv:
        x = x.replace('\n','')
        entry = x.split(',')
        patienten_lijst.append(entry)
    """append een lijst met de header wegeghaald"""

    lijst_med_a = list()
    lijst_med_b = list()
    """append een lijst """

    for x in patienten_lijst:
        lijst_med_a.append(int(x[1]))
        lijst_med_b.append(int(x[2]))

    print(lijst_med_a)
    print(lijst_med_b)
    """voegt de waardes toe in grfaiek"""

    x_as = lijst_med_a
    y_as = lijst_med_b



    naam = ['aantal medicijnen']
    plt.xlabel('Hoeveelheid medicijnen')
    plt.ylabel('Hoeveelheid totaal aantal medicijn')
    plt.scatter(x_as, y_as, )

    plt.show()
main()