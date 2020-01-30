import matplotlib.pyplot as plt
#Auteur: Gijsbert Keja
#Datum: November 2019
def main():
    een()
    """
    de main roept de funtie aan
    """


def een():
    """
    Deze functie geeft 2 variabelen een waarde waarna deze in een lijst
gepusht worden en gebruikt worden om de staafdiagram te maken en te weergeven
:param: geen
:return: geen
"""
    janssen = 5
    Berends = 5


    hoogte = [5, 5]  # maakt de hoogte voor de staven
    naam = ['Berends', 'Janssen']  # geeft de staven een naam

    plt.bar(range(len(hoogte)), hoogte, tick_label= naam )
    plt.show()

main()
