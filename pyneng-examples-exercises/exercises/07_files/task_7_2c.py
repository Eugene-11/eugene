# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']
from sys import argv
g = open(argv[2], 'w')
with open (argv[1], 'r') as f:
    for line in f:
        if line.find(ignore[0]) is not -1 or line.find(ignore[1]) is not -1 or line.find(ignore[2]) is not -1:
            continue
        else: 
            with open (argv[2], 'a') as h:
                h.write(line)
