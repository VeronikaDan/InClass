import re
f = open('tyams.txt', 'r', encoding = 'utf-8')
s = f.read()
words = s.split()
count = len(words)
i = 0
regexp = '((Т|т)ям[п]?(ы|е|а|ами))'
reg = '[аеоуиюяэыё]'
for word in words:
    if re.search(regexp, word):
        i += 1
        res = re.search(regexp, word)
        print(res.group(1))
print('тямов в тексте ' + str(i))
a = re.findall(reg, s)
print('гласных - ' + str(len(a)))

