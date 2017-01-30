import re
import time

start_time = time.time()

def comms_raw():
    f = open('names_mystemmed.txt','r',encoding='utf-8')
    a = f.readlines()
    names = []
    for line in a:
        m = re.search('(.*){',line)
        if m:
            name = m.group(1)
            names.append(name)
    print(names)
    types = []
    for line in a:
        m = re.search('имя|фам',line)
        if m:
            type = m.group(0)
            types.append(type)
    print(types)
#    for line in a:




#    with open('commands.txt', 'w',encoding='utf-8') as file:
#        for comm_raw in comms_raw:
#            command = 'INSERT INTO names (ID,name,type,gender) VALUES ' + '(' + comm_raw + ')' + ';\n'
#            file.write(command)



def main():
    comms_raw()
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()