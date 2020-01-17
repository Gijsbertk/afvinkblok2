import re
openen = open('Mus_musculus.GRCm38.pep.all.fa', 'r')
protein_lijst = list()
seq = ''

for regel in openen:
    if not regel.startswith(">") or regel.startswith(" "):
        seq += regel.rstrip()

print(seq)

#fout = re.search(r"[^ 'ACDEFGHIKLMNPQRSTVWY]", seq)
#if fout:
#    print("Een foute nucleotide gevonden")
 #   print("Nucleotide " + fout.group())
  #  print("Op positie " + fout.start())

#else:
    #print('eiwit klopt')

