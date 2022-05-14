"""
1. List filtering.
Дан объект типа list():

l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

Релизуйте функцию которая отфильтрует только integer (int) значения из этого списка.

Напишите несколько вариантов решения:
•	используя цикл for
•	используя list comprehensions
•	используя filter() + lambda

Пример:
def filter_list(l):
    return  # [1, 2, 4, 10, 33]

Check yourself:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""


def filter_list_for(lst):
    """Filtering using For cycle"""
    filtered_list = []
    for i in lst:
        if type(i) is int:
            filtered_list.append(i)
    return filtered_list


def filter_list_comprehension(lst):
    """Filtering using List Comprehension"""
    filtered_list = [i for i in lst if type(i) is int]
    return filtered_list


def filter_list_lambda(lst):
    """Filtering using filter() + lambda"""
    filtered_list = filter(lambda a: type(a) is int, lst)
    return list(filtered_list)


if __name__ == '__main__':
    l = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]

    assert filter_list_for([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list_for([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list_for([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

    assert filter_list_comprehension([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list_comprehension([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list_comprehension([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]

    assert filter_list_lambda([1, 2, 'a', 'b']) == [1, 2]
    assert filter_list_lambda([1, 'a', 'b', 0, 15]) == [1, 0, 15]
    assert filter_list_lambda([1, 2, 'aasf', '1', '123', 123]) == [1, 2, 123]




