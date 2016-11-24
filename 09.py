import re
f = open('china.txt', 'r', encoding = 'utf-8')
s = f.read()
reg = '(«.+?»)'
m = re.findall(reg, s)
for name in m:
    if re.search('[йъьжшх]', name):
        print(name)




