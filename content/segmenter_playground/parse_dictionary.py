import re


# https://regex101.com/r/vC86NV/1
PATTERN = r'^([^ ]+) ([^ ]+) \[([^]]+)] /(.+)/'

for line in open('cedict_ts.u8').readlines()[:1000]:
    traditional, simplified, pronunciation, translation = re.match(PATTERN, line).groups()
    print(translation)
