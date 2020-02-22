import re
from collections import Counter


segmented = open('segmented_book.txt').readlines()
PUNCTUATION = "！？｡。＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

c = Counter()
for line in segmented:
    words = re.sub(rf'[{PUNCTUATION}]+', ' ', line).split()
    c.update(words)

print(c.most_common(5000))
print(f'{len(c)}=')
