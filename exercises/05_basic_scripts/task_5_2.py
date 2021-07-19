# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


print ('\nЗадание 5.2:\n')
address = input ('Введите адрес:')
mask = address.split('/')[1]
mask2 = '1' * int(mask) + '0' * (32 - int(mask) )
ip = address.split('/')[0].split('.')


network = '{0:08b}{1:08b}{2:08b}{3:08b}'
network = (network.format(int(ip[0]),int(ip[1]), int(ip[2]),int(ip[3])))
network = network[0:int(mask)+1]
minus = 32 - int(mask)
network = str(network + "0" * minus)
network = network[0:8]+ ' ' + network[8:16] + ' ' + network[16:24] + ' ' + network[24:32]
network = network.split(' ')
network = str(int(network[0], 2)) + '.' + str(int(network[1], 2)) + '.' + str(int(network[2], 2)) + '.' + str(int(network[3], 2))
network = network.split('.')
#print (network)

Network = '''\nNetwork:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print (Network.format(int(network[0]),int(network[1]), int(network[2]),int(network[3])))

octet1 = int(mask2[0:8], 2)
octet2 = int(mask2[8:16], 2)
octet3 = int(mask2[16:24], 2)
octet4 = int(mask2[24:32], 2)

Mask = '''Mask:
/{0}
{5:<8} {6:<8} {7:<8} {8:<8}
{1:<8} {2:<8} {3:<8} {4:<8}

'''

stdout = Mask.format(mask, mask2[0:8], mask2[8:16], mask2[16:24], mask2[24:32], octet1, octet2, octet3, octet4)
print(stdout)
