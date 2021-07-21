# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]
file = open('config_sw1.txt', 'r').readlines()
stop =len(file)
stdout = []
ignore = set(ignore)

for f in range(stop):
        if str(file[f]).startswith('!'):
            pass
        elif ignore.intersection(file[f].split()):
            pass
        else:
            stdout.append(file[f])

print(''.join(stdout))
