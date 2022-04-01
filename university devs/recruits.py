"""
Сопоставить списки одинаковой длины и найти тех, кто является призывником.

Первый - имена студентов, позволяющие их точно идентифицировать. 
Второй — год рождения. 
Третий — пол студента.
Часть данных утрачены. 
"""

from data import names, bday_years, genders


def get_recruits(names, bday_years, genders):
    """
    Принимает три списка одинаковой длины.
    Возвращает список с именами студентов мужского пола, которые достигли или могут достигнуть 18 лет в 2021 году, 
    но при этом не старше 30 лет.
    Cтуденты, по которым невозможно точно установить информацию, попадают в отдельный список.
    """
    def is_rec(student):
        """
        Идентифицирует тех, кто точно является призывником
        """
        if not student[1] or not student[2]:
            return False

        age = 2021 - student[1]
        is_rec_age = 30 >= age >= 18
        if student[2] == 'Male' and is_rec_age:
            return True


    def is_mb_rec(student):
        """
        Идентифицирует тех, кто возможно является призывником
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