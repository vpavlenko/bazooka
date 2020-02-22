import re


lines = open('hpmor_cn_saved.txt').readlines()

buckets = ['']

for line in lines:
    if re.match("第.+章[：: ]", line):
        print('NEWCHAPTER')
    else:
        print(line)

# for i, bucket in enumerate(buckets, 1):
#     with open(f'segmenter_playground/chapters/{i:03d}_input.txt', 'w') as output_file:
#         output_file.write(bucket)
