"""
logging & argparse.
Для задания importlib, реализуйте логирование в консоль и файл одновременно.

Примечания:
• если пакет не найден, логгер должен записать строку “Package not found” в ERROR level.
• для найденного пакета, логгер должен записать описание пакета (метод __doc__) в WARNING, путь к пакету в INFO и
версию пакета в DEBUG.
• уровень логирования задается отдельно для консоли и отдельно для файла через параметры командной строки,
используя библиотеку argparse.
"""

from importlib import util, import_module
import logging
import argparse


def add_logger(console_level, file_level):
    # create logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # create console handler
    ch = logging.StreamHandler()
    ch.setLevel(level=console_level)

    # create file handler
    fh = logging.FileHandler('file.log')
    fh.setLevel(level=file_level)

    logger.warning(f'Logging Level: console - {console_level}, file - {file_level}')

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # add handler to logger
    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def get_package_path(package_name):
    is_found = util.find_spec(package_name)     # returns object if package was found, otherwise - None
    if is_found is not None:
        imported_package = import_module(package_name)
        Logger.warning(f'Doc: {imported_package.__doc__}')
        Logger.info(f'Path: {imported_package.__file__}')
        try:
            Logger.debug(f'Version: {imported_package.__version__}')
        except AttributeError:
            Logger.debug('Version not found')
        package_path = is_found.origin
    else:
        Logger.error('Package not found')
        package_path = 'Package not found'
    return package_path


def parse_cmd_args():
    parser = argparse.ArgumentParser('Search package and select logging level')
    log_levels = ['NOTSET', 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('--console', default='DEBUG', choices=log_levels, help='logging level for console')
    parser.add_argument('--file', default='DEBUG', choices=log_levels, help='logging level for file')

    cmd, _ = parser.parse_known_args()

    return cmd.console, cmd.file


if __name__ == '__main__':
    args = parse_cmd_args()
    Logger = add_logger(*args)
    package = input('Enter package name: ')
    get_package_path(package)
