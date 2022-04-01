"""
Найти студетов, которые могут поехать на соревнования.
Требования: спортсмен, знает английский, старше 20 лет.
"""

from data import speak_english, sports, older_than_20


def find_athlets(*args):
    """
    Функция возвращает список имен студентов, которые подходят под все три критерия
    """
    s = [set(arg) for arg in args]
    result = s[0].intersection(s[1], s[2])
    return list(result)


athletes = find_athlets(speak_english, sports, older_than_20)