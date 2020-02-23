import re
from collections import Counter

from parse_dictionary import get_translation


KNOWN_WORDS = 200

segmented = open('segmented_book.txt').readlines()[:1000]
PUNCTUATION = "！？｡。＂＃＄％＆＇（）＊-＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

c = Counter()
for line in segmented:
    words = re.sub(rf'[{PUNCTUATION}]+', ' ', line).split()
    c.update(words)

print(c.most_common(KNOWN_WORDS))
print(f'{len(c)}=')

print('')
print('KNOWN WORDS')
known_words = set()
for word, _ in c.most_common(KNOWN_WORDS):
    print(word, get_translation(word))
    known_words.add(word)
print('/KNOWN WORDS')
print()

DEBUG = False

for line in segmented[:20]:
    print(line)
    line = line[:-1] + ' '
    word = ''
    for character in line:
        # print(f'{character=}')
        if character in PUNCTUATION:
            if DEBUG:
                print('char:       ', character)
            else:
                print(character, end=' ')
            word = ''
        elif character == ' ':
            if word:
                if word in known_words:
                    if DEBUG:
                        print('known word: ', word)
                    else:
                        print(word, end=' ')
                else:
                    # print(f'{word=}')
                    translation = get_translation(word, debug=DEBUG)
                    if translation[0] == '*':
                        translation = ' '.join([get_translation(c, debug=DEBUG) for c in word])
                    if DEBUG:
                        print('translation:', translation)
                    else:
                        print(translation, end=' ')
                word = ''
        else:
            word += character
    print()
    print()
