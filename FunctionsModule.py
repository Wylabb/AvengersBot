import importlib
from importlib import reload

import id


def backup():
    f = open('id.py')
    data = f.read()
    f.close()
    f = open('backup.py', 'w')
    f.write(data)
    f.close()


def genlist(line):
    c = '\n'
    for i in range(len(line)):
        k = i + 1
        c += str(k) + '. ' + line[i][:-1] + '\n'
    return c


def geninfo(line):
    c = '\n'
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
        k = i + 1
        c += str(k) + '. ' + line[i][16:] + '\n'
    return c


def gensell(line):
    c = '\n'
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
        k = i + 1
        c += str(k) + '. ' + line[i] + '\n'
    return c


def search(line):
    importlib.reload(id)
    if hasattr(id, str(line)):
        return 1
    else:
        return 0


def deepsearch(word):
    deeplist = [line for line in open('id.py') if word in line]
    for i in range(len(deeplist)):
        deeplist[i] = deeplist[i][:-1]
    if deeplist:
        return deeplist
    else:
        return ['________________Пусто_']


def getvalue(word):
    if word == '________________Пусто_':
        return 0
    else:
        reload(id)
        var = list(word.split(sep=' '))
        var = str(var[-1])
        return int(var)


def create(line):
    f = open('id.py', 'a+')
    line = line + ' = 0\n'
    f.write(line)
    f.close()
    reload(id)


def edit(line, newvalue):
    f = open('id.py')
    data = f.read()
    oldvalue = getattr(id, line)
    data = data.replace(line + ' = ' + str(oldvalue), line + ' = ' + str(newvalue))
    f.close()
    f = open('id.py', 'w')
    f.write(data)
    f.close()


def add(line, change):
    reload(id)
    f = open('id.py')
    data = f.read()

    oldvalue = getattr(id, line)
    newvalue = oldvalue + int(change)
    data = data.replace(line + ' = ' + str(oldvalue), line + ' = ' + str(newvalue))
    f.close()
    f = open('id.py', 'w')
    f.write(data)
    f.close()


def delite(line):
    f = open('id.py')
    data = f.read()
    oldvalue = getattr(id, line)
    data = data.replace(line + ' = ' + str(oldvalue), '')
    f.close()

    f = open('id.py', 'w')
    f.write(data)
    f.close()
    with open('id.py', 'rw') as file:
        for line in file:
            if not line.isspace():
                file.write(line)
