"""
2.	Find min. and max. value.
Имеется список:
numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]
Преобразуйте элементы списка в тип int(). Найдите минимальное и максимальное значение.
"""

numbers = [1, 2, '0', '300', -2.5, 'Dog', True, 0o1256, None]

integers = []

for i in numbers:
    try:
        integers.append(int(i))
    except Exception as e:                   # skip "i" if not integerable
        continue

print(integers)
print("Min:", min(integers))
print("Max:", max(integers))

