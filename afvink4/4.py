import re
sequence = 'ATGGTAGGACGTTGCTGACAGCTGACAGCT'
pattern = '([ATCG]{3})'
print(re.split(pattern, sequence))