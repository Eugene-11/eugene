# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
with open (argv[1], 'r') as f:
    for line in f:
        if line.startswith('!') or line.find(ignore[0]) is not -1 or line.find(ignore[1]) is not -1 or line.find(ignore[2]) is not -1:
            continue
        else:
            print(line.strip())

