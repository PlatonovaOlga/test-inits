"""
Who will enter the university on a competitive basis?

Each entrant has the results of exams in maths, Russian and computer science.
There are also extra points.

Need to select 20 people whose total score is higher than the others.
If it is not possible to uniquely identify 20 people 
(for example, 2 people scored the same TOTAL number of scores and claim
on the 20th place in the list, it is worth ranking them 
according to the "profile" disciplines - "computer science" and "mathematics"). 
"""

from operator import itemgetter
from heapq import nlargest

from data import entrants


def find_top_20(entrants):
    """
    Accepts a list of summary information on entrants and returns a list with the names of 20 people,
    those with the highest TOTAL score who will become students of the university. 
    """
    if len(entrants) <= 20:
        return [c.get('name') for c in entrants]

    e_scored = list()

    for person in entrants:
        p = dict(
                name=person.get('name'),
                total=sum([s for s in person.get('scores').values()]) + person.get('extra_scores'),
                computer_science=person.get('scores').get('computer_science'),
                math=person.get('scores').get('math'))
        e_scored.append(p)

    e_sorted = sorted(
        e_scored, 
        key=itemgetter('total'), 
        reverse=True)

    e_top_20 = e_sorted[:20]
    
    # is there at least one other entrant with a score equal to the student's score in 20th place? 
    if e_sorted[19].get('total') == e_sorted[20].get('total'):
        lucky = nlargest(1, e_sorted[19:], key=itemgetter('total', 'computer_science', 'math'))
        e_top_20[19] = lucky[0]

    return [c.get('name') for c in e_top_20]


students = find_top_20(entrants)