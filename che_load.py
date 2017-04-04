import sqlite3

con = sqlite3.connect('demo.db')
cur = con.cursor()

import urllib.request, json

url = u'https://api.vk.com/method/wall.get?owner_id=-53845179'
res = urllib.request.urlopen(url).read().decode('utf-8')
wall = json.loads(res)
wall = wall['response'][1:]
print(len(wall))
##texts = {}
##comments = {}
##for i in range(20):
##    if i != 0:
##        post_id = wall[i]['id']
##        li = [wall[i]['text'], wall[i]['likes']['count']]
##        texts[post_id] = li
##        for offset in [0, 100]:
##            url_comm = u'https://api.vk.com/method/wall.getComments?owner_id=-53845179&post_id='+str(post_id)+'offset='+str(offset)
##            res_comm = urllib.request.urlopen(url_comm).read().decode('utf-8')
##            comm = json.loads(res_comm)
              
    
f = open('wall_che.json', 'w', encoding='utf-8')
json.dump(wall, f, indent = 2, ensure_ascii = False)
f.close()

#cur.execute('create table users (id int primary key, name varchar(100))')
#con.commit()

#cur.execute('insert into users (id, name) values (1, "Veronika")')
#con.commit()

#cur.execute('select * from users')
#print(cur.fetchall())
