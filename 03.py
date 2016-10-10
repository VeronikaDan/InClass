f = open('text1.txt', 'r', encoding = 'utf-8')
i = 1
a = f.readlines()
for line in a:
    print("длина строки " + str(i) + " - " + str(len(line)))
    i += 1
a3 = a[3::3]
for line in a3:
    print(line)
f.close()
