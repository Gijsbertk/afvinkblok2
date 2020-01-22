import matplotlib.pyplot as plt
def main():
    een()
    """de main roept de funties aan """

def een():
    patienten_csv = open('patienten.csv','r')
    header = patienten_csv.readline()
    patienten_data = list()
    """leest opent bestand en maakt een lijst aan """

    for x in patienten_csv:
        x = x.replace('\n','')
        entry = x.split(',')
        patienten_data.append(entry)
    """append een lijst met de header wegeghaald"""
    lijst_patienten = list()
    lijst_med_a = list()
    kleur_lijst = ()
    """append een lijst """

    for x in patienten_data:
        lijst_patienten.append(int(x[0]))
        lijst_med_a.append(int(x[1]))
        if x[3] == "Janssen":
            kleur_lijst += ('blue', )
        if x[3] == "Berends":
            kleur_lijst += ('red', )

            """voegt de waardes toe in grfaiek"""

    artsen = ['Janssen','Berends']
    hoogte = lijst_med_a
    naam = lijst_patienten
    plt.xlabel('Patiënt nummer')
    plt.ylabel('Hoeveelheid medicijn')
    plt.bar(range(len(hoogte)), hoogte, tick_label= naam , color=kleur_lijst)
    plt.show()
main()