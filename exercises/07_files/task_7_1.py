# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


file = open('ospf.txt', 'r').readlines()

for ospf_route in file:

    gogo = ospf_route.split(',')
    gaga = gogo[0].split()

    Router = {
        'Prefix': gaga[1],
        'AD/Metric': gaga[2],
        'Next-Hop': gaga[4],
        'Last update': gogo[1].strip(),
        'Outbound Interface': gogo[2].strip()
    }
    print ("{:30}{:30}".format("Prefix:", str(Router['Prefix'])))
    print ("{:30}{:30}".format("AD/Metric:", str(Router['AD/Metric'])))
    print ("{:30}{:30}".format("Next-Hop:", str(Router['Next-Hop'])))
    print ("{:30}{:30}".format("Last update:", str(Router["Last update"])))
    print ("{:30}{:30}".format("Outbound Interface:", str(Router["Outbound Interface"])))
    print('\n')