import re

seq = 'ACTYARARYTACATCRACATY'



code = re.search((r'A[CT]NYR', seq))
if code:
    print('Hij doet het')