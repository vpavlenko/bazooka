import re
from collections import Counter

LEARNING_RATE = 8
MIN_NUM_REPETITIONS_ON_ITER = 10

lines = open('hpmor_cn_saved.txt').readlines()

buckets = ['']

for line in lines:
    if re.match("第.+章[：: ]", line):
        buckets.append('')
        print(line)
    else:
        buckets[-1] += line

known_chars = set()
for i, bucket in enumerate(buckets):
    c = Counter(bucket)
    for char in known_chars:
        del c[char]
    learning_rate = LEARNING_RATE if i > 5 else 20
    new_chars, new_chars_count = zip(*c.most_common(learning_rate))
    if i > 5:
        if new_chars_count[0] >= MIN_NUM_REPETITIONS_ON_ITER:
            while new_chars_count[-1] < MIN_NUM_REPETITIONS_ON_ITER:
                learning_rate -= 1
                new_chars, new_chars_count = zip(*c.most_common(learning_rate))
        # else:
        #     print()
        #     print(f'SKIP BATCH {i=}')
        #     print()
        #     continue
    known_chars_count = sum(char in known_chars for char in bucket)
    unknown_chars_count = len(bucket) - known_chars_count - sum(new_chars_count)
    print(f'{new_chars=}, {new_chars_count=}, {sum(new_chars_count)=}, {learning_rate=}')
    print(f'bucket {i=}, {len(bucket)=}, {known_chars_count=}')
    print(f'{known_chars_count/len(bucket)=:.4f}, {sum(new_chars_count)/len(bucket)=:.4f}, {unknown_chars_count/len(bucket)=:.4f}')
    print()
    known_chars.update(new_chars)

print(len(buckets))
