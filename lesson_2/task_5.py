"""
Unix 'ls -lh' on Python.
По аналогии с командой ls -lh для Unix систем, реализуйте модуль на Python который отображает содержимое директории

Примечания:
•	Чтобы получить содержимое директории используйте os.listdir
•	Используйте os.stat чтобы получить информацию о каждом файле
•	Используйте библиотеку prettytable
1.	pip install prettytable
2.	Имена столбцов: Mode, Owner, Group, Size, File name
•	Используйте библиотеки pwd и grp чтобы получить имя пользователя и группу
"""

from prettytable import PrettyTable
import pwd
import grp
import os, sys

# add Lesson_1 path to system path for import of function file_size() from Lesson_1/task_4.py
os.chdir('..')
sys.path.append(os.getcwd())
from Lesson_1 import Task_4


def ls_lh(path):
    """Display content of current folder"""
    content = os.listdir(path)
    for i in content:
        if not i.startswith('.'):
            stat = os.stat(os.path.join(path, i))
            uid = pwd.getpwuid(stat.st_uid).pw_name
            gid = grp.getgrgid(stat.st_gid).gr_name
            x.add_row([stat.st_mode, uid, gid, Task_4.file_size(stat.st_size), i])
    x.align['Size'] = 'r'
    x.align['File name'] = 'l'
    x.sortby = 'File name'
    print(x)


## List Comprehension
# def ls_lh(path):
#     lst = [[os.stat(os.path.join(path, i)).st_mode,
#             os.stat(os.path.join(path, i)).st_uid,
#             os.stat(os.path.join(path, i)).st_gid,
#             os.stat(os.path.join(path, i)).st_size,
#             i] for i in os.listdir(path) if not i.startswith('.')]
#     for l in lst:
#         l[1] = pwd.getpwuid(l[1]).pw_name
#         l[2] = grp.getgrgid(l[2]).gr_name
#     x.add_rows(lst)
#     x.sortby = 'File name'
#     print(x)


# pth = r'C:/Users/Igor_Minenka/PycharmProjects/py-test-automation/Lesson_1'

if __name__ == '__main__':
    x = PrettyTable()
    x.field_names = ['Mode', 'Owner', 'Group', 'Size', 'File name']

    pth = input('Enter path: ')
    ls_lh(pth)

