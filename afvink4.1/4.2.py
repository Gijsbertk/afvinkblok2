import re
import time
"""creeërt de tijd"""

start_time = time.time()


"""main functie"""

def main():
    een() = seq
    twee(seq)


"""functie maakt het bestand open en stript daarna de header eraf"""


def een():
    openen = open('Mus_musculus.GRCm38.dna.chromosome.1.fa', 'r')
    protein_lijst = list()
    seq = ''

    for regel in openen:
        if not regel.startswith(">") or regel.startswith(" "):
            seq += regel.rstrip()

"""funtie kijkt of er een fout zit in het dna  """

def twee(seq):
    fout = re.search((r'[^ATCG]', seq))

    if fout:
        print('Er is een fout gevonden')
        print('De fout is '+ fout.group())
        print('Op positie '+ fout.start())

    verlopen_tijd = time.time() - start_time
    print(verlopen_tijd)

main()