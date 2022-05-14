"""1.	Multiply numbers with regex.
Дан текст:

Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных

Напишите функцию которая умножает каждую цифру в тексте на 2, и возвращает изменённый текст

Example:
def my_function(text, multiplier=2):
    # implement me
    return text

my_function('I am 10 years old')
'I am 20 years old'

my_function('I am 10 years old', multiplier=25)
'I am 250 years old'

Примечания:
•	используйте re.sub https://docs.python.org/3/library/re.html#re.sub
•	обратите внимание на параметр repl (repl can be a string or a function)
"""
import re


def my_function(text, multiplier=2):
    pattern = r'[0-9]+'
    multiply_func = lambda a: str(int(a.group()) * multiplier)
    text = re.sub(pattern, multiply_func, text)
    return text


if __name__ == '__main__':

    text_example = "Из 35 футболистов, забивших как минимум 7 голов на чемпионатах мира, только у троих футболистов" \
                   " средний показатель превышает 2 гола за игру. Эти 35 игроков представляют 14 футбольных сборных"

    print(my_function('I am 10 years old'))
    print(my_function(text_example))
    print(my_function('I am 10 years old', multiplier=25))




