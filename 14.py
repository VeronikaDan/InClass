import re
import json

def getText(fileName):
    f = open(fileName, 'r', encoding = 'utf-8')
    alltext = f.read()
    text = re.findall('[а-яА-Я]+', alltext)
    textLow = []
    for word in text:
        textLow.append(word.lower())
    return textLow

def getArticles():
    listOfArticles = ['Под конец 2016 года стали видны контуры новой сборной России по футболу - Черчесов _ Футбол _ Р-Спорт. Все главные новости спорта..html',
                      'Станислав Черчесов_ «Сборная России прибавляет в физическом плане, ее игра обретает контуры» _ ЗвездаРУ_ Футбольные новости.html',
                      'ТАСС_ Спорт - Черчесов_ у сборной России по футболу появляются контуры новой команды.html']
    words = {}
    for i in range(3):
        words[i] = getText(listOfArticles[i])
    return words

def listOfNewspapers():
    listOfNewspapers = ['Р-Спорт', 'Звезда', 'ТАСС']
    newspapers = {}
    for i in range(3):
        newspapers[i] = listOfNewspapers[i]
    return newspapers

def writeCommon():
    data = getArticles()
    dataCommon = set(data[0]) & set(data[1]) & set(data[2])
    f = open('common.json', 'w')
    json.dump(list(dataCommon), f, indent = 2, ensure_ascii = False)
    f.close()

def commonOfPairs():
    np = listOfNewspapers()
    words = getArticles()
    data = {}
    for i in range(3):
        for k in range(3):
            if i is not k:
                key = np[i] + '+' + np[k]
                data[key] = set(words[i]) & set(words[k])
    return data

if __name__ == '__main__':
    writeCommon()
    commonOfPairs()
