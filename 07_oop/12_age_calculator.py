# get date of birth from user and calculate age in years, months and days

from datetime import datetime

class AgeCalculator:
    def __init__(self, dob):
        self.dob = dob

    def calculate_age(self):
        today = datetime.today()
        dob = datetime.strptime(self.dob, '%Y-%m-%d')
        age = today - dob
        years = age.days // 365
        months = (age.days % 365) // 30
        days = (age.days % 365) % 30
        return years, months, days


dob = 1993-6-24
age = AgeCalculator(dob)
years, months, days = age.calculate_age()
print(f'You are {years} years, {months} months and {days} days old')