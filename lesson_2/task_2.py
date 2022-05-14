"""
IP validation.
Напишите функцию для валидации IP-адреса.

Пример:
def check_ip(ip_address):
    return Tue/False

Напишите несколько вариантов решения:
•	используя библиотеку re
•	используя socket.inet_aton

Check yourself
assert check_ip('') is False
assert check_ip('192.168.0.1') is True
assert check_ip('0.0.0.1') is True
assert check_ip('10.100.500.32') is False
assert check_ip(700) is False
assert check_ip('127.0.1') is True
"""

import re
import socket


def check_ip_re(ip_address):
    """Check value is IP address using library Re"""
    valid_ip = False
    ip_regex = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')
    match = ip_regex.fullmatch(str(ip_address))
    if match:
        for i in match.group().split('.'):
            if int(i) <= 255:
                valid_ip = True
            else:
                valid_ip = False
                break
    return valid_ip


def check_ip_socket(ip_address):
    """Check value is valid ip using library socket.inet_aton"""
    ip_address = str(ip_address)
    is_valid = False
    if ip_address.count('.') == 3:
        try:
            socket.inet_aton(ip_address)
            is_valid = True
        except socket.error:
            print('Incorrect IP range:', ip_address)
    else:
        print('Incorrect IP format:', ip_address)
    return is_valid


if __name__ == '__main__':
    assert check_ip_re('') is False
    assert check_ip_re('192.168.0.1') is True
    assert check_ip_re('0.0.0.1') is True
    assert check_ip_re('10.100.500.32') is False
    assert check_ip_re(700) is False

    assert check_ip_socket('') is False
    assert check_ip_socket('192.168.0.1') is True
    assert check_ip_socket('0.0.0.1') is True
    assert check_ip_socket('10.100.500.32') is False
    assert check_ip_socket(700) is False
