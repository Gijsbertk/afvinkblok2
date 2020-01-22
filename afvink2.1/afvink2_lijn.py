import matplotlib.pyplot as plt
def main():
    een()
    """de main roept de funties aan """

def een():
    """leest opent bestand en maakt een lijst aan """
    patienten_csv = open('patienten.csv','r')
    header = patienten_csv.readline()
    patienten_lijst = list()

    for x in patienten_csv:
        x = x.replace('\n','')
        entry = x.split(',')
        patienten_lijst.append(entry)

    lijst_patienten = list()
    lijst_med_a = list()
    """append een lijst met de header wegeghaald"""
    for x in patienten_lijst:
        lijst_patienten.append(int(x[0]))
        lijst_med_a.append(int(x[1]))

    x = lijst_patienten
    y = lijst_med_a
    """append een lijst """

    plt.ylabel('De hoeveelheid medicijn')
    plt.xlabel('Patiënt')
    plt.plot(x, y)
    plt.show()


main()