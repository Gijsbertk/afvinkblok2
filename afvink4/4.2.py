import re
import time
start_time = time.time()
openen = open('Mus_musculus.GRCm38.dna.chromosome.1.fa', 'r')
protein_lijst = list()
seq = ''

for regel in openen:
    if not regel.startswith(">") or regel.startswith(" "):
        seq += regel.rstrip()



fout = re.search((r'[^ATCG]', seq))
if fout:
    print('Er is een fout gevonden')
    print('De fout is '+ fout.group())
    print('Op positie '+ fout.start())

verlopen_tijd = time.time() - start_time
print(verlopen_tijd)