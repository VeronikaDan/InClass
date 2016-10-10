f = open('text1.txt', 'r', encoding = 'utf-8')
words = f.read()
d = {}
words = words.replace('(', '')
words = words.replace(')', '')
words = words.replace('[', '')
words = words.replace(']', '')
w = words.split()
for word in w:
    word = word.strip('.,!?')
    word = word.lower()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
for word in sorted(d):
    print(word, d[word])
