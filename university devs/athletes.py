"""
Find all students who can go to competitions.
Requirements: athlete, speaks English, over 20 years old. 
"""

from data import speak_english, sports, older_than_20


def find_athlets(*args):
    """
    Returns a list of student's names, that match all three criteria
    """
    s = [set(arg) for arg in args]
    result = s[0].intersection(s[1], s[2])
    return list(result)


athletes = find_athlets(speak_english, sports, older_than_20)