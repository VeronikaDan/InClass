import random

def randomword(file):
    f = open(file, 'r',encoding = 'utf-8')
    m = f.readlines()
    word = random.choice(m)
    return word.strip()

def line2():
    subj = randomword('who.txt') + ' '
    adv = randomword('how.txt') + ' '
    pred = randomword('verb.txt') + ' '
    where = randomword('where.txt') + '.'
    s = subj + adv + pred + where + '\n'
    return s

def manyline2():
    i = random.randint(1,3)
    s = ''
    for a in range(i):
        s = s + line2()
    return s

def main():
    haiku = randomword('when.txt') + '\n' + manyline2() + randomword('feel.txt')
    print(haiku)
    
if __name__ == '__main__':
    main()
    
    
    
