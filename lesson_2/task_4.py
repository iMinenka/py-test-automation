#!/usr/bin/env python
"""
Unix `find' on Python.
По аналогии с Unix утилитой find, реализуйте модуль на Python для поиска файлов и директорий на файловой системе.

Обратите внимание на скрипт find_util

bash$ ./find_util /usr/ -name "*.pyc" -type f

Где "*.pyc" есть паттерн имени файл(ов) в формате shell-pattern

Примечания:
•	используйте os.walk
•	используйте os.path.join
•	для проверки имени файла на соответствие паттерну используйте fnmatch.
"""

import sys
import argparse
import os
from fnmatch import fnmatch


def find(folder, name=None, show_dirs=True, show_files=True):
    """
    :param folder: path to a system folder from where to start searching
    :param name: file/directory name pattern, allows using '*' and '?' symbols
    :param show_dirs: if True - include directories into search results
    :param show_files: if True - include files into search results
    """
    # Generate files and dirs tree of a folder
    for root, dirs, files in os.walk(folder, topdown=True):

        if show_dirs:  # search by folder name
            for dir in dirs:
                if fnmatch(dir, name):
                    print(os.path.join(root, dir))

        if show_files:  # search by file name
            for file in files:
                if fnmatch(file, name):
                    print(os.path.join(root, file))


def parse_cmd_args():
    path_help = "Path to a folder"
    name_help = "File name pattern. Allows using '*' and '?' symbols"
    type_help = "Where 'f' means search only files, 'd' means only directories"

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help=path_help)
    parser.add_argument('-name', nargs='?', default=None, help=name_help)
    parser.add_argument('-type', nargs='?', default=None, choices=['f', 'd'], help=type_help)

    if len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    cmd, _ = parser.parse_known_args()

    files, dirs = True, True
    if cmd.type == 'd':
        files = False
    if cmd.type == 'f':
        dirs = False
    return cmd.path, cmd.name, dirs, files


if __name__ == '__main__':
    args = parse_cmd_args()
    find(*args)

# python3 task_4.py /mnt/c/Users/Igor_Minenka/Documents/Python/Homework/ -name "*folder" -type d