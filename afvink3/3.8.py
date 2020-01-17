import pickle
groenten = {'Broccoli':2.50, 'Bloemkool':1.50, 'Kool':1.00, 'Wortel':3.50, 'Spruiten':2.75, 'Spinazie':3.50}
print(groenten)


vraag = input('Wilt u een nieuwe groete toevoegen? Zo ja typ dan j: ')

if vraag == 'j':
    je_groente = input('Vul je groenten in: ')
    prijs = int(input('Vul de van prijs  de groenten in: '))
    groenten[je_groente] = prijs
    print(groenten)
    vraag = input('Wilt u een nieuwe groete toevoegen? Zo ja typ dan j: ')
