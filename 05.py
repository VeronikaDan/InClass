f = open('05text.txt', 'w', encoding = 'utf-8')
stroka = 'куку'
while stroka != 'стоп':
    stroka = input('напишите слово: ')
    i = str(len(stroka))
    endings = ['ть','шь','ем','им','ют','ут','ят','ит','ет','те','ла','ло','ли','л']
    b = False
    m = []
    for letter in stroka:
        m.append(letter)
    m2 = m[::-1]
    if stroka != 'стоп':
        f.write(stroka + ';' + i)
        if m == m2:
            f.write(';' + 'палиндром;')
        else:
            f.write(';' + 'не палиндром;')
        for i in range(14):
            if stroka.endswith(endings[i]):
                f.write('глагол\n')
                b = True
        if b == False:
            f.write('не глагол\n')
        
f.close()
