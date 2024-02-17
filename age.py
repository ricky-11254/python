import time
import datetime

class Age:
    def __init__(self):
        pass
    def calculate(self):
        current_date = datetime.datetime.now()
        current_year = current_date.year
        years = current_year - 1956
        return years

age_calculate = Age()
years = age_calculate.calculate()
print(years)
