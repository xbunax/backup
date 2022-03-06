class Date:
    def __init__(self,year,month,day):
        self.year=year
        self.month=month
        self.day=day
    def get_year(self):
        return year
    def get_date(self):
        return year,month,day
    def get_month(self):
        return month

date=Date(2018,12,12)
print(date.day)