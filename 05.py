f = open('05text.txt', 'w', encoding = 'utf-8')
stroka = 'hello'
while stroka != 'stop':
    stroka = input('print smth: ')
    i = str(len(stroka))
    m = []
    for letter in stroka:
        m.append(letter)
    m2 = m[::-1]
    if stroka != 'stop':
        f.write(stroka + ';' + i)
        if m == m2:
            f.write(';' + 'yes' + '\n')
        else:
            f.write(';' + 'no' + '\n')
f.close()
