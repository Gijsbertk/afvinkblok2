import matplotlib.pyplot as plt
def main():
    een()
    """de main roept de funties aan """


def een():
    """vriabelen krijgt functie geeft de grfaiek waarde mee activeert hem en geeft labels"""

    janssen = 5
    Berends = 5


    hoogte = [5, 5]
    naam = ['Berends', 'Janssen']

    plt.bar(range(len(hoogte)), hoogte, tick_label= naam )
    plt.show()

main()