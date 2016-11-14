import os
m = os.listdir('C:/Users/student/Desktop/python')
countFiles = {}
for file in m:
    if file.endswith('.txt') & (file is not '06text.txt'):
        f = open(file, 'r', encoding = 'utf-8')
        words = f.read()
        w = words.split()
        dic = []
        for word in w:
            word = word.strip('.,!?«»')
            word = word.lower()
            if word not in dic:
                dic.append(word)
            if word in countFiles:
                countFiles[word] +=1
            else:
                countFiles[word] = 1
        
f2 = open('06text.txt','w',encoding='utf-8')
for word1 in countFiles:
    if countFiles[word1] > 1:
        f2.write(word1 + ' - ' + str(countFiles[word1]) + '\n')
f.close()
f2.close()
