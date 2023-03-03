# Задача 1
# Дано имя файла: folder1/folder2/file.ext
# Необходимо вывести на экран его расширение с помощью стандартного модуля re.
import re

filename = input('Введите имя файла: ')
pattern = '\..*'
a = re.search(pattern, filename)
print(a.group())
