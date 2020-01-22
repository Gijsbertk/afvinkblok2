import re

"""main functie"""


def main():
    een() = seq
    twee(seq)

    """functie maakt het bestand open en stript daarna de header eraf"""


def een():
    openen = open('Mus_musculus.GRCm38.pep.all.fa', 'r')
    protein_lijst = list()
    seq = ''

    for regel in openen:
        if not regel.startswith(">") or regel.startswith(" "):
            seq += regel.rstrip()

print(seq)
"""funtie kijkt of er een fout zit in het eiwit  """

def twee(seq):
    fout = re.search(r"[^ 'ACDEFGHIKLMNPQRSTVWY]", seq)
    if fout:
        print("Een foute nucleotide gevonden")
        print("Nucleotide " + fout.group())
        print("Op positie " + fout.start())

    else:
        print('eiwit klopt')

main()