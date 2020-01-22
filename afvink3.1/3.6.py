def main():
    """main functie roept de andere aan  """

    lezen()

def lezen():
    """opent het bestand en leest het in """

    lezen1 = open('1.txt','r')
    lezen2 = open('2.txt','r')
    """geeft ze een set mee """

    text1 = set(lezen1)
    text2 = set(lezen2)
    alles = text1.union(text2)
    print(alles)
    """nieuwe sets door sets bij elkaar op te tellen of af te trekken """
    overeenkomst = text1 & (text2)
    print(overeenkomst)

    verschil = text1 - text2
    print(verschil)

    verschil2 = text2 - text1
    print(verschil2)

    bijzonder = text1.symmetric_difference(text2)
    print(bijzonder)

main()