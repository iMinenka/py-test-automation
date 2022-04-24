"""
3.	Letters Count.
Имеется текст:

Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years.
Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.
Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!

Определите какая буква наиболее часто встречается в этом тексте и сколько раз в этом тексте встречается слово 'Python'?

Примечания:
•	не учитывайте регистр букв, т.е. 'A' = 'a'
•	не учитывайте знаки препинания и спецсимволы (кавычки, тире)
•	не учитывайте пробелы и переводы строк
"""

text = """Python is an interpreted high-level programming language for general-purpose programming. Created by Guido 
van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using 
significant whitespace. It provides constructs that enable clear programming on both small and large scales. In July 
2018, the creator Guido Rossum stepped down as the leader in the language community after 30 years. Python features a 
dynamic type system and automatic memory management. It supports multiple programming paradigms, including 
object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library. Python 
interpreters are available for many operating systems. CPython, the reference implementation of Python, 
is open source software and has a community-based development model, as do nearly all of Python's other 
implementations. Python and CPython are managed by the non-profit Python Software Foundation. Привет из Харькова!"""


letters = dict()

for i in text.lower():
    if i.isalpha():                 # symbol from text is letter
        if i not in letters:
            letters[i] = 1
        else:
            letters[i] += 1
    else:                           # is not letter
        continue

print("Letter frequency in text:", letters)

topValue = max(letters.values())
index_topValue = list(letters.values()).index(topValue)
topLetter = list(letters)[index_topValue]

print("Most frequent letter:", topLetter, letters[topLetter])

print("Python occurred in text:", text.lower().count("python"))

