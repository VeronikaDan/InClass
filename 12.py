import os

def walker():
    for root, dirs, files in os.walk('C:/Users/Public'):
        print(files)

def takeAlpha():
    alphaGruz = {}
    alpha = open('alphabet_gruz.txt', 'r', encoding = 'utf-8')
    for stroka in alpha:
        stroka = stroka.split()
        alphaGruz[stroka[0]] = stroka[1]
    alpha.close()
    return alphaGruz

def readText():
    f = open('gruz_text1.txt', 'r', encoding = 'utf-8')
    text = f.read()
    letterList = list(text)
    f.close()
    return letterList

def convertToIPA():
    f = open('gruz_text_IPA.txt', 'w', encoding = 'utf-8')
    letterList = readText()
    ipa = takeAlpha()
    for letter in letterList:
        if letter in ipa:
            letter = ipa[letter]
        f.write(letter)
    f.close()
    

if __name__ == '__main__':
    convertToIPA()
    
    
