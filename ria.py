import urllib.request
import re
import json
import lxml.html

def getTree(url):
    req = urllib.request.urlopen(url)
    html = req.read().decode('utf-8')
    tree = lxml.html.fromstring(html)
    return tree

def cicle():
    year = ['2015','2016']
    month = ['01','02','03','04','05','06','07','08','09','10','11','12']
    interval = 'июль 15 - декабрь 16'
    themes = ['politics', 'defense_safety', 'society', 'media', 'health',
              'education', 'beauty_medicine', 'economy', 'company', 'world',
              'incidents', 'sport', 'science', 'technology', 'culture', 'religion']
    refs = []
    return refs

def getMeta(tree):
    title = tree.xpath('.//title/text()')[0].replace(' | РИА Новости - события в России и мире: темы дня, фото, видео, инфографика, радио','')
    date = tree.xpath('.//head/meta[@property="article:published_time"]')[0].get('content')
    
    return title

def getText(tree):
    ps = tree.xpath('.//div[@itemprop="articleBody"]/p/text()')
    text = ''
    for sent in ps:
        sent = sent.replace('/ха0',' ')
        text = text + sent
    return text

def writeInJson(dic):
    f = open('dic.json', 'w')
    json.dump(dic, f, indent = 2, ensure_ascii = False)
    f.close()            

if __name__ == '__main__':
    tree = getTree('https://ria.ru/science/20170201/1486964975.html')
    meta = getMeta(tree)
    print(meta)
