"""
Определить, кто поступит в университет на конкурсной основе. 

У абитуриента есть результаты экзаменов по математике, русскому и информатике. 
Также есть дополнительные баллы.

Нужно отобрать 20 человек, у которых суммарный балл выше, чем у других. 
В случае, если не получается однозначно определить 20 человек 
(например, 2 человека набрали одинаковое СУММАРНОЕ количество баллов и претендуют 
на 20 место в списке, стоит их ранжировать по "профильным" дисциплинам - "информатике" и "математике").
"""

from operator import itemgetter
from heapq import nlargest

from data import entrants


def find_top_20(entrants):
    """
    Принимает список сводной информации по абитуриентам и возвращает список с именами 20 человек, 
    набравших наибольшее СУММАРНОЕ количество баллов, которые станут студентами университета.
    """
    # если мест достаточно всем:
    if len(entrants) <= 20:
        return [c.get('name') for c in entrants]

    # преобразую исходные данные: оставлю три показателя, избавлюсь от вложенного словаря
    e_scored = list()

    for person in entrants:
        p = dict(
                name=person.get('name'),
                total=sum([s for s in person.get('scores').values()]) + person.get('extra_scores'),
                computer_science=person.get('scores').get('computer_science'),
                math=person.get('scores').get('math'))
        e_scored.append(p)

    # отсортирую по сумме баллов по убыванию
    e_sorted = sorted(
        e_scored, 
        key=itemgetter('total'), 
        reverse=True)

    # выберу топ-20
    e_top_20 = e_sorted[:20]
    
    # есть ли как минимум еще один абитуриент с суммой баллов, равной баллу студента на 20 месте?
    if e_sorted[19].get('total') == e_sorted[20].get('total'):
        lucky = nlargest(1, e_sorted[19:], key=itemgetter('total', 'computer_science', 'math'))
        e_top_20[19] = lucky[0]

    return [c.get('name') for c in e_top_20]


students = find_top_20(entrants)