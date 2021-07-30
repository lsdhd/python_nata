# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_int_vlan_map (config_filename):
    openfile = open(config_filename, 'r')
    access = {}
    trunk = {}
    for f in openfile:
            if str(f).startswith('interface'):
                interface = f.split(' ')[1].strip()
            elif 'access vlan' in f:
                vlan_access = f.split(' ')[-1]
                access[interface] = vlan_access.strip()
            elif 'trunk allowed' in f:
                vlan_trunk = f.split(' ')[-1]
                trunk[interface] = vlan_trunk.strip()
            elif 'mode access' in f:
                access[interface] = 1
    return (access, trunk)
print(get_int_vlan_map('config_sw2.txt'))
