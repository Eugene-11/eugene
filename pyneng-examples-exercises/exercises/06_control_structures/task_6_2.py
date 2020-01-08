# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Enter IP, please, in 10.0.1.1 format:')
ip1 = ip.split('.')
d0, d1, d2, d3 = list(map(int, ip1))
if 0<d0<224:
        print("unicast")
elif 223<d0<=239:
        print('multicast')
elif d0==d1==d2==d3==255:
        print('local broadcast')
elif d0==d1==d2==d3==0:
        print('unassigned')
else:
        print("unused")
