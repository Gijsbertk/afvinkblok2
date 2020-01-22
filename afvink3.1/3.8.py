import pickle
def main():
    """de main roept de funties aan """

    dict() = groenten
    invul(groenten)


def dict():
    """dic wordt aangemaakt """

    groenten = {'Broccoli':2.50, 'Bloemkool':1.50, 'Kool':1.00, 'Wortel':3.50, 'Spruiten':2.75, 'Spinazie':3.50}
    print(groenten)

def invul(groenten):
    """een input waarmee de nieuwe groenten voor de dic kan worden toegevoegd"""

    vraag = input('Wilt u een nieuwe groete toevoegen? Zo ja typ dan j: ')
    if vraag == 'j':
        je_groente = input('Vul je groenten in: ')
        prijs = int(input('Vul de van prijs  de groenten in: '))
        groenten[je_groente] = prijs
        print(groenten)
        vraag = input('Wilt u een nieuwe groete toevoegen? Zo ja typ dan j: ')

main()