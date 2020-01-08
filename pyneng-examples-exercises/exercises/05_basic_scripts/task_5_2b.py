# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ip_mask = argv[1]
old_list = ip_mask.split('/')
ip = old_list[0].split('.')         
mask = int(old_list[1])
d0, d1, d2, d3 = list(map(int, ip)) 
m = '1'*mask + '0'*(32-mask)
oct1 = m[0:8]
oct2 = m[8:16]
oct3 = m[16:24]
oct4 = m[24:32]
octet1 = (int(oct1[0])*2**7 + int(oct1[1])*2**6 + int(oct1[2])*2**5+ int(oct1[3])*2**4 + int(oct1[4])*2**3 + int(oct1[5])*2**2 + int(oct1[6])*2**1 + int(oct1[7])*2**0)
octet2 = (int(oct2[0])*2**7 + int(oct2[1])*2**6 + int(oct2[2])*2**5+ int(oct2[3])*2**4 + int(oct2[4])*2**3 + int(oct2[5])*2**2 + int(oct2[6])*2**1 + int(oct2[7])*2**0)
octet3 = (int(oct3[0])*2**7 + int(oct3[1])*2**6 + int(oct3[2])*2**5+ int(oct3[3])*2**4 + int(oct3[4])*2**3 + int(oct3[5])*2**2 + int(oct3[6])*2**1 + int(oct3[7])*2**0)
octet4 = (int(oct4[0])*2**7 + int(oct4[1])*2**6 + int(oct4[2])*2**5+ int(oct4[3])*2**4 + int(oct4[4])*2**3 + int(oct4[5])*2**2 + int(oct4[6])*2**1 + int(oct4[7])*2**0)
print(f'''
          ...: Network:
          ...: {d0:<10} {d1:<10} {d2:<10} {d3:<10}  
          ...: {d0:08b}   {d1:08b}   {d2:08b}   {d3:08b}
          ...: Mask:
          ...: /{mask}
          ...: {octet1:<10} {octet2:<10} {octet3:<10} {octet4:<10}  
          ...: {octet1:08b}   {octet2:08b}   {octet3:08b}   {octet4:08b}''')
