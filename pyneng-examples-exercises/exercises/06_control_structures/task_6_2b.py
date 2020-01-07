'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
IP_correct = False
ip = input('Enter IP, please, in 10.0.1.1 format:\n')
while not IP_correct:
    dot = ip.count('.')
    ip2 = ip.split('.')
    if dot == 3:
        for i in ip2:
            if i.isdigit() and 0<=int(i)<=255:
                pass
            else:
                print('Неправильный IP-адрес')
                ip = input('Enter IP again, please:\n')
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
            IP_correct = True
    else:
        print('Неправильный IP-адрес')
        ip = input('Enter IP again, please:\n')





