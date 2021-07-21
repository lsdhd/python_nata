# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file = open('config_sw1.txt', 'r').readlines()
stop =len(file)
stdout = []
ignore = ["duplex", "alias", "configuration"]
ignore = set(ignore)

for f in range(stop):
        if str(file[f]).startswith('!'):
            pass
        elif ignore.intersection(file[f].split()):
            pass
        else:
            stdout.append(file[f])

result = open('result.txt', 'w')
result.write(''.join(stdout))
result.close()


