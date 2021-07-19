# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
print('\nЗадание 6.2b\n')


while True:
    ip = input("Введите адрес:").split('.')
    good_ip = len(ip) ==4

    for i in ip:
        good_ip = i.isdigit() and int(i) >=0 and int(i) <= 255
    if good_ip:
        break
    print('Неправильный ip адрес.')

if int(ip[0]) <= 223 and int(ip[0]) > 0:
    print('Unicast')
elif int(ip[0]) >= 224 and int(ip[0]) <= 239:
    print('multicast')
elif int(ip[0]) == 255 and int(ip[1]) == 255 and int(ip[2]) == 255 and int(ip[3]) == 255:
    print('local broadcast')
elif int(ip[0]) == 0 and int(ip[1]) == 0 and int(ip[2]) == 0 and int(ip[3]) == 0:
    print('unassigned')
else:
    print('unused')