# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
g = open('config_sw1_cleared.txt', 'w')
with open (argv[1], 'r') as f:
    for line in f:
        if line.find(ignore[0]) is not -1 or line.find(ignore[1]) is not -1 or line.find(ignore[2]) is not -1:
            continue
        else: 
            with open ('config_sw1_cleared.txt', 'a') as h:
                h.write(line)
