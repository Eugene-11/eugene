# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Enter IP in 10.0.1.1 format:\n')
dot = ip.count('.')
ip2 = ip.split('.')
if dot == 3:
        for i in ip2:
            if i.isdigit() and 0<=int(i)<=255:
                pass
            else:
                print('Неправильный IP-адрес')
                break
        else:
            if 0<int(ip2[0])<224:
                print("unicast")
            elif 223<int(ip2[0])<=239:
                print('multicast')
            elif int(ip2[0])==int(ip2[1])==int(ip2[2])==int(ip2[3])==255:
                print('local broadcast')
            elif int(ip2[0])==int(ip2[1])==int(ip2[2])==int(ip2[3])==0:
                print('unassigned')
            else:
                print("unused")
else:
    print('Неправильный IP-адрес')

