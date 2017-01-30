import os
import re
import time

start_time = time.time()


def task1():
    directory = '/Users/sea_fog/Documents/github/Exam2017/subs'
    files = os.listdir(directory)
    n = open('allsubs.txt', 'w', encoding='utf-8')
    m = str()
    for file in files:
        f = open(directory + '/' + file, 'r', encoding='utf-8')
        m = m + f.read()
        f.close()
    n.write(m)
    allsubs_dir = '/Users/sea_fog/Documents/github/Exam2017/allsubs.txt'
    allsubs_mystemmed = '/Users/sea_fog/Documents/github/Exam2017/allsubs_mystemmed.txt'
    os.system('./mystem -ni ' + allsubs_dir + ' ' + allsubs_mystemmed)
    f = open('allsubs_mystemmed.txt', 'r', encoding='utf-8')
    a = f.readlines()
    f.close()
    for line in a:
        name_marker = re.compile(r'S,.*имя|фам')
        lines = []
        if name_marker.search(line):
            lines.append(line)
            for newline in lines:
                capitals = re.compile(r'^[А-Я].*')
                f = open('names_mystemmed.txt', 'a', encoding='utf-8')
                if capitals.search(newline):
                    f.write(newline)
                f.close()
    n = open('names_mystemmed.txt', 'r', encoding='utf-8')
    m = n.readlines()
    n.close()
    names = list(set(m))
    n_names = []
    for name in names:
        k = re.search('(.*){', name)
        if k:
            name = k.group(1)
            n_names.append(name)
    f_names = sorted(n_names)
    l = open('allnames.txt', 'a', encoding='utf-8')
    for f in f_names:
        print(f)
        l.write(f + '\n')
    print('\n')
    return f_names


def task2(f_names):
    f = open('plot.txt', 'r', encoding='utf-8')
    a = f.read()
    f.close()
    for name in f_names:
        if name in a:
            print(name)


def main():
    task2(task1())
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
    
