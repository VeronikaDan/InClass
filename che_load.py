import urllib.request, json

url = u'https://api.vk.com/method/wall.get?owner_id=-53845179'
res = urllib.request.urlopen(url).read().decode('utf-8')
wall = json.loads(res)
texts = {}
comments = {}
for i in range(100):
    if i != 0:
        post_id = wall['response'][i]['id']
        li = [wall['response'][i]['text'], wall['response'][i]['likes']['count']]
        texts[post_id] = li
        url_comm = u'https://api.vk.com/method/wall.getComments?owner_id=-53845179&post_id='+str(post_id)
        res_comm = urllib.request.urlopen(url_comm).read().decode('utf-8')
        comm = json.loads(res_comm)
              
    
f = open('wall_che.json', 'w', encoding='utf-8')
json.dump(wall, f, indent = 2, ensure_ascii = False)
f.close()

