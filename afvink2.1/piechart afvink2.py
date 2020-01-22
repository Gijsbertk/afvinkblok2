import matplotlib.pyplot as plt

def main():
    een()
    """de main roept de funties aan """

def een():
    """leest opent bestand en maakt een lijst aan """

    patienten_csv = open('patienten.csv','r')
    header = patienten_csv.readline()
    patienten_lijst = []

    """append een lijst met de header wegeghaald"""

    for x in patienten_csv:
        x = x.replace('\n','')
        entry = x.split(',')
        patienten_lijst.append(int(entry[2]))

    vijftig = 0
    veertig = 0
    dertig = 0
    """append een lijst met de header wegeghaald"""

    lijst_med_b = list()

    """append een lijst """

    for x in patienten_lijst:
        if x >= 50:
            vijftig += 1
        elif x <50 and x >= 40:
            veertig += 1
        elif x < 40:
            dertig += 1

    """voegt labels toe"""


    labels = 'dertig', 'veertig', 'vijftig'
    sizes = [dertig, veertig, vijftig]

    plt.pie(sizes, labels=labels)

    plt.show()
main()