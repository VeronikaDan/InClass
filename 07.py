import re
f = open('1.txt', 'r', encoding = 'utf-8')
s = f.read()
words = s.split()
count = len(words)
i = 0
regexp = '[А-ЯЁа-яё]'
for word in words:
    if re.search(regexp, word):
        i += 1
if count != i:
    print(i, count)
else:
    print(count)

