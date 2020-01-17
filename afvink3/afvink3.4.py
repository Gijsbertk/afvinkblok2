import random
een = 0
twee = 0
drie = 0
vier = 0
vijf = 0
zes = 0
zeven = 0
acht = 0
negen = 0
tien = 0

cijfer_lijst = list()
for x in range(100):
    nummer = random.randint(1 , 10)
    cijfer_lijst.append(nummer)
print(cijfer_lijst)

for x in cijfer_lijst:
    if x == 1:
        een += 1
    elif x == 2:
        twee += 1
    elif x == 3:
        drie += 1
    elif x == 4:
        vier += 1
    elif x == 5:
        vijf += 1
    elif x == 6:
        zes += 1
    elif x == 7:
        zeven += 1
    elif x == 8:
        acht += 1
    elif x == 9:
        negen += 1
    elif x == 10:
        tien += 1

print(negen)
dick = {}
dick['Een'] = een
dick['Twee'] = twee
dick['drie'] = drie
dick['vier'] = vier
dick['vijf'] = vijf
dick['zes'] = zes
dick['zeven'] = zeven
dick['acht'] = acht
dick['negen'] = negen
dick['Tien'] = tien
print(dick)