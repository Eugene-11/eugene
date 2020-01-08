# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
a = ospf_route.replace(',','').split()
b = a.remove('via')
print (f"""
       ...: Protocol: {a[0].replace('O', 'OSPF')}
       ...: Prefix: {a[1]} 
       ...: AD/Metric: {a[2].strip('[]')} 
       ...: Next-Hop: {a[3]}
       ...: Last update: {a[4]}
       ...: Outbound interface: {a[5]} """)
