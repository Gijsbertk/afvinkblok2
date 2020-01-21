import re


class Rna:

    def __init__(self, sequentie, naam):

        self.__gen_naam = naam
        zoekterm = "[AUCGN]"
        if re.search(zoekterm, sequentie) is not None:
            self.__sequentie = sequentie

    def get_translation(self):
        return self.__sequentie


class Dna:

    def __init__(self, sequentie):
        zoekterm = "[ATCGN]"
        if re.search(zoekterm, sequentie) is not None:
            self.__sequentie = sequentie

    def set_dna(self, sequentie):
        zoekterm = "[ATCGN]"
        if re.search(zoekterm, sequentie) is not None:
            self.__sequentie = sequentie
        else:
            print("Geen geldige sequentie opgegeven")

    def get_dna(self):
        return self.__sequentie

    def get_transcript(self):

        rna = ""
        for i in range(len(self.__sequentie)):
            if self.__sequentie[i] == "A":
                rna += "U"
            if self.__sequentie[i] == "T":
                rna += "A"
            if self.__sequentie[i] == "C":
                rna += "G"
            if self.__sequentie[i] == "G":
                rna += "C"
            if self.__sequentie[i] == "N":
                rna += "N"
        return rna

    def get_lengte(self):
        return len(self.__sequentie)

    def gc_percentage(self):
        gc = self.__sequentie.count("G") + self.__sequentie.count("C")
        gc_procent = (gc / self.__sequentie.count("")) * 100
        return gc_procent


def main():
    dna_lijst = []
    langste = 0
    index = 0
    headers, seqs = lees_bestand("Felis_catus.Felis_catus_8.0.cdna.all.fa")
    for i in range(len(seqs)):
        dna_lijst.append(Dna(seqs[i]))
        lengte = dna_lijst[i].get_lengte()
        if lengte > langste:
            langste = lengte
            index = i
    print("Het langste gen is gen: " + headers[index] + " met een lengte van: " + str(dna_lijst[index].get_lengte()))
    print("Met een GC% van " + str(dna_lijst[index].gc_percentage()))
    if str(input("Wil je het transcript ook zien? ")) == "ja":
        print("Het transcript is: " + str(dna_lijst[index].get_transcript()))


def lees_bestand(bestands_naam):
  
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


main()
