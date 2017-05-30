import urllib.request, json

class VKmember():
    def __init__(self, no, name, wall):
        self.id = no
        self.fullname = name
        self.wallcount = wall

class VKuser(VKmember):
    def __init__(self, no, name, sx, wall):
        VKmember.__init__(self, no, name, wall)
        self.sex = sx

class VKgroup(VKmember):
    def __init__(self, no, name, wall, member):
        VKmember.__init__(self, no, name)
        self.members = member

def get_wall(no):
    url = 'https://api.vk.com/method/wall.get?&extended=1&owner_id=' + no
    res = urllib.request.urlopen(url).read().decode('utf-8')
    wall = json.loads(res)
    wall_count = wall['response']['wall'][0]
    name = wall['response']['groups'][0]['name']

def get_user(no):
    url = 'https://api.vk.com/method/users.get?fields=sex&user_id=' + no
    res = urllib.request.urlopen(url).read().decode('utf-8')
    user = json.loads(res)
    user = user['response'][0]
    name = user['last_name'] + ' ' + user['first_name']
    if user['sex'] == 2:
        sx = 'male'
    else:
        sx = 'female'
