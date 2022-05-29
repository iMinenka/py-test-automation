"""1.	Using threading library to verify URL's.
В файле links.txt содержится список url-адресов которые нужно провалидироавть на доступность.

Нам необходимо наиболее эффективное решение. Используйте библиотеку threading, чтобы инициировать множество web-запросов одновременно.

Результат выполнения скрипта сохраните в файл в формате JSON (см. пример ниже)

Примечание:
•	Используйте библиотеку requests (pip install requests)
•	Проперти Response.ok может быть полезной для определения валидности респонза (github/requests)

Пример результата:

[
  {
    "url": "https://www.does_not_exist.com/",
    "is_ok": false,
    "status_code": null
  },
  {
    "url": "http://lucumr.pocoo.org/",
    "is_ok": true,
    "status_code": 200
  },
  {
    "url": "http://jinja.pocoo.org/docs/",
    "is_ok": true,
    "status_code": 200
  }
]
"""
import json
import logging
import requests
import threading

import urllib3.exceptions

logging.basicConfig(level=logging.INFO)


def read_file(name):
    """This function reads a file containing links. Expecting one link per row.

    Args:
        name (str): the name of the file to read

    Returns:
        list: list of rows read from file

    Raises:
        FileNotFoundError: if provided file cannot be found

    """
    try:
        with open(name, 'r') as txt_file:
            file_data = txt_file.read().split('\n')
    except FileNotFoundError as e:
        if not FileNotFoundError:
            raise
        logging.error(f'File not found. Error: {e}')
    else:
        return file_data


def validate_url(url, results):
    """This function checks if url is valid and gets its status code.
    Then puts the result into dictionary and adds the dictionary to the list with other results.

    Args:
        url (str): link to be verified
        results (list): list to store the results for verified urls

    Raises:
        Exception: if url is unreachable (for example, ConnectionError, MissingSchema)

    """
    url_result = {'url': url, 'is_ok': False, 'status_code': None}

    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError as e:
        logging.warning(f'Cannot open {url}. Error: {e}')
    except requests.exceptions.MissingSchema as e:
        logging.warning(f'Invalid url {url}. Error: {e}')
    else:
        url_result['is_ok'] = response.ok
        url_result['status_code'] = response.status_code
    finally:
        results.append(url_result)


def write_file(data):
    """This function receives final links results and writes in a json file.

    Args:
        data (list): list of dictionaries representing results for each link

    """
    with open('result.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)


if __name__ == '__main__':
    links = read_file('links.txt')
    links_results = list()

    threads = []

    for link in links:
        t = threading.Thread(target=validate_url, args=(link, links_results))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    write_file(links_results)
