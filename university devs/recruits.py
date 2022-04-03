"""
Match lists of the same length and find those who are recruits.

The first is the names of the students, allowing them to be accurately identified.
The second is the year of birth.
The third is the gender of the student.
Part of the data is lost. 
"""

from data import names, bday_years, genders


def get_recruits(names, bday_years, genders):
    """
    Accepts three lists of the same length.
    Returns a dict with two items: 
    1. list with the names of male students who are or may be 18 years of age in 2021,
    but not older than 30 years.
    2. Students for whom it is impossible to accurately establish information. 
    """
    def is_rec(student):
        """
        Identifies those who are definitely recruits 
        """
        if not student[1] or not student[2]:
            return False

        age = 2021 - student[1]
        is_rec_age = 30 >= age >= 18
        if student[2] == 'Male' and is_rec_age:
            return True


    def is_mb_rec(student):
        """
        Identifies those who maybe are definitely recruits 
        """
        if student[2] == 'Female' or is_rec(student):
            return False

        if student[1]:
            age = 2021 - student[1]
            is_rec_age = 30 >= age >= 17
            return is_rec_age

        return True


    recruits = list(filter(
        is_rec, 
        zip(names, bday_years, genders)))

    maybe_recruits = list(filter(
        is_mb_rec, 
        zip(names, bday_years, genders)))    
        
    return dict(
        recruits=[r[0] for r in recruits],
        maybe_recruits=maybe_recruits)
    

result = get_recruits(names, bday_years, genders)