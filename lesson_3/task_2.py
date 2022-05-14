"""
importlib
Используя библиотеку importlib, реализуйте функцию, которая будет возвращать путь к пакету, если он установлен,
и строку “Package not found” – если нет.

Пример:

def get_package_path(package_name):
    # implement me
    return package_path
"""
from importlib import util


def get_package_path(package_name):
    is_found = util.find_spec(package_name)     # returns object if found, otherwise None
    if is_found is not None:
        package_path = is_found.origin
    else:
        package_path = 'Package not found'
    return package_path


if __name__ == '__main__':
    package = input('Enter package name: ')
    print(get_package_path(package))
