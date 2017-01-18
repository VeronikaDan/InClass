import urllib.request
import re
import json

def getHtml(url):
    req = urllib.request.urlopen(url)
    html = req.read().decode('windows-1251')
    return html

def getRefs():
    main_page = getHtml('https://www.gazeta.ru/science/')
    reg = '/science/2017/01/[0-9]{2}_a_[0-9]+\.shtml'
    r = re.findall(reg, main_page)
    mn = set(r)
    refs = []
    for e in mn:
        refs.append('https://www.gazeta.ru' + e)
    return refs

def getText(html):
    t = html.split('article_text')[1]
    t1 = t.split('article_pants')[0]
    reg = '<p>.+</p>'
    sent = re.findall(reg, t1)
    text = ''
    for s in sent:
        text += s[3:-4]
    return text

def makeDic(refs):
    texts = []
    for ref in refs:
        texts.append(getText(ref))
    reg = '[а-яА-ЯёЁъ]+'
    dic = {}
    for text in texts:
        w = re.findall(reg, text)
        for word in w:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    return dic

def writeInJson(dic):
    f = open('dic.json', 'w')
    json.dump(dic, f, indent = 2, ensure_ascii = False)
    f.close()            

if __name__ == '__main__':
    refs = getRefs()
    dic = makeDic(refs)
    writeInJson(dic)
