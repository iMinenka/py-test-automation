"""
4.	File size conversion.
Релизуйте функцию которая принимает размер файла в байтах (Byte) и преобразует его в удобный для чтения формат: Byte, Kilobyte, Megabyte, Gigabyte.

Пример:

def file_size(size_in_bytes):
    # implement me
    return '12.6Mb'

Примечания:
•	Стоит ограничиться Гигабайтами
•	String Format examples:
https://docs.python.org/3/library/string.html#format-examples
•	это очень плохая реализация: https://stackoverflow.com/a/14822210

Ответьте на вопрос:
•	Сколько гигабайт (Gigabyte) в sys.maxsize ?

Check yourself:

assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'
"""

import sys


# Approach 1 - initial
def file_size(size_in_bytes):
    size = size_in_bytes
    if size_in_bytes < 1024:
        size = f"{round(size_in_bytes / 1, 1)}B"
    elif size_in_bytes < 1048576:
        size = f"{round(size_in_bytes / 1024, 1)}Kb"
    elif size_in_bytes < 1073741824:
        size = f"{round(size_in_bytes / 1048576, 1)}Mb"
    elif size_in_bytes <= sys.maxsize:
        size = f"{round(size_in_bytes / 1073741824, 1)}Gb"
    else:
        size = f"Out of allowed sys.maxsize: {sys.maxsize}"
    return size


assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'


# Approach 2
def file_size(size_in_bytes):
    size_name = ['B', 'Kb', 'Mb', 'Gb']
    n = 1024
    size = size_in_bytes
    for i in size_name:
        if size_in_bytes <= n ** (size_name.index(i) + 1):
            size = f"{round(size_in_bytes / n ** (size_name.index(i)), 1)}" \
                   f"{size_name[size_name.index(i)]}"
            break
        elif size_in_bytes <= sys.maxsize:
            size = f"{round(size_in_bytes / n ** (size_name.index(i) + 1), 1)}" \
                   f"{size_name[size_name.index(i)]}"
        else:
            size = f"Out of allowed sys.maxsize: {sys.maxsize}"
    return size


assert file_size(19) == '19.0B'
assert file_size(12345) == '12.1Kb'
assert file_size(1101947) == '1.1Mb'
assert file_size(572090) == '558.7Kb'
assert file_size(999999999999) == '931.3Gb'

# print(sys.maxsize / 1024 ** 3, "Gb")
# print(sys.maxsize)
