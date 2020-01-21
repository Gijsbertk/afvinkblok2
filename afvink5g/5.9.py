class trivia:

    def __init__(self, __punten1, __punten2):
        self.__punten1 = __punten1
        self.__punten2 = __punten2

    def vragen(self):
        antwoord = 'a'
        print('Beurt aan speler1')
        print('#vraag1')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten1 = + 1

        antwoord = 'a'
        print('Beurt aan speler1')
        print('#vraag2')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten1 = + 1

        antwoord = 'a'
        print('Beurt aan speler1')
        print('#vraag3')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten1 = + 1

        antwoord = 'a'
        print('Beurt aan speler1')
        print('#vraag4')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten1 = + 1

        antwoord = 'a'
        print('Beurt aan speler1')
        print('#vraag5')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten1 = + 1

        antwoord = 'a'
        print('Beurt aan speler2')
        print('#vraag6')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten2 = + 1

        antwoord = 'a'
        print('Beurt aan speler2')
        print('#vraag7')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten2 = + 1

        antwoord = 'a'
        print('Beurt aan speler2')
        print('#vraag8')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten2 = + 1

        antwoord = 'a'
        print('Beurt aan speler2')
        print('#vraag9')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten2 = + 1

        antwoord = 'a'
        print('Beurt aan speler2')
        print('#vraag10')
        print('')
        print('')
        print('')
        print('')
        vraag = input('wat is het antwoord?: ')
        if vraag == antwoord:
            self.__punten2 = + 1

    def punten(self):
        if self.__punten1 > self.__punten2:
            print('Speler 1 is winnaar!')
        if self.__punten1 == self.__punten2:
            print('Gelijkspel!')
        if self.__punten1 < self.__punten2:
            print('Speler 2 is winnaar')


spelen = trivia(0, 0)
spelen.vragen()

print(spelen.punten())
