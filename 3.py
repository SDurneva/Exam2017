import re
import time

start_time = time.time()

def comms_rawf():
    f = open('names_mystemmed.txt','r',encoding='utf-8')
    a = f.readlines()
    names = []
    for line in a:
        m = re.search('(.*){',line)
        if m:
            name = m.group(1)
            names.append(name + ', ')
    print(len(names))
    IDs1 = list(range(len(names)))
    IDs = []
    for id in IDs1:
        id = str(id) + ', '
        IDs.append(id)
    print(len(IDs))
    types = []
    for line in a:
        m = re.search('имя|фам',line)
        if m:
            type = m.group(0)
            types.append(type + ', ')
    print(len(types))
    genders = []
    for line in a:
        g = re.search('муж|жен|мж',line)
        if g:
           gender = g.group(0)
           genders.append(gender + ', ')
    print(len(genders))
    print(names)
    print(types)
    print(genders)
    comms_raw = ['{}{}{}{}'.format(x, y, z, n) for x, y, z, n in zip(IDs, names, types, genders)]
    return comms_raw

def make_inserts(comms_raw):
    with open('commands.txt', 'w',encoding='utf-8') as file:
        for comm_raw in comms_raw:
            command = 'INSERT INTO names (ID,name,type,gender) VALUES ' + '(' + comm_raw + ')' + ';\n'
            file.write(command)



def main():
    make_inserts(comms_rawf())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()