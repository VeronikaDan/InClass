def takeAlpha():
    alphaAmh = {}
    alpha = open('amh_alphabet.txt', 'r', encoding = 'utf-8')
    k = 0
    for stroka in alpha:
        stroka = stroka.split()
        if k == 0:
            vowels = list(stroka)
        for i in range(7):
            if not k == 0:
                alphaAmh[stroka[i+1]] = stroka[0] + vowels[i]
        k = 1
    alpha.close()
    print(alphaAmh)
    return alphaAmh

def readText():
    f = open('amh_text1.txt', 'r', encoding = 'utf-8')
    text = f.read()
    letterList = list(text)
    f.close()
    return letterList

def convertToIPA():
    f = open('amh_text_IPA.txt', 'w', encoding = 'utf-8')
    letterList = readText()
    ipa = takeAlpha()
    for letter in letterList:
        if letter in ipa:
            letter = ipa[letter]
        f.write(letter)
    f.close()
    

if __name__ == '__main__':
    convertToIPA()
