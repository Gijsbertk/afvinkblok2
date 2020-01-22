import re
"""main functie  """

def main()
    seq = 'ACTYARARYTACATCRACATY'
    een()



"""funtie kijkt of er een fout zit in het dna  """

def een():
    code = re.search((r'A[CT]NYR', seq))
    if code:
        print('Hij doet het')