"""1.	Singleton pattern. Расширить реализацию задания по Company model.
Реализовать паттерн синглтон для нового класса Alex, который наследуется от Engineer, и
написать юнит-тесты для проверки того, что паттерн работает правильно. """

from lesson_4.task_3 import Engineer


# Option 1
class Alex(Engineer):
    """Create singleton pattern using baseclass and method __new__"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


# Option 2
class Singleton(type):
    """Create metaclass for Singleton pattern with __call__"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Bill(Engineer, metaclass=Singleton):
    """Create new class Bill using Singleton metaclass."""
    pass


