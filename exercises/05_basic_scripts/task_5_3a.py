# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

print('\nЗадание 5.3\n')

mode = input('Введите режим работы интерфейса (access, trunk):')
interface = input('Введите тип и номер интерфейса:')

access_template = [
     "switchport mode access", "switchport access vlan {0}",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable", "Введите номер VLAN: "
]

trunk_template = [
    "switchport trunk encapsulation dot1q", "switchport mode trunk",
    "switchport trunk allowed vlan {0}",'','', 'Введите разрешенные VLANы: '
]

tag = {
    'trunk': trunk_template,
    'access': access_template
    }

vlan = input(tag[mode][5])

print ('\n', '-' * 30)
print(' Interface ', interface)
print ('\n',tag[mode][0],'\n',tag[mode][1].format(str(vlan)),'\n',tag[mode][2].format(str(vlan)),'\n',tag[mode][3],'\n',tag[mode][4])