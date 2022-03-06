from ex9_1 import Student
class HighSchoolStudent(Student):
    def __init__(self,name,age,Chin,Math,Engl,Phys,Chem,Biol,Hist,Poli):
        Student.__init__(self,name,age,Chin,Math,Engl)
        self.Physics=Phys
        self.Chemistry=Chem
        self.Biology=Biol
        self.History=Hist
        self.Politics=Poli
    def get_average(self):
        sum=self.Chinese+self.Math+self.English
        sum=sum+self.Biology+self.Chemistry+self.History+self.Physics+self.Politics
        return sum/8
    def get_max_course(self):
        max=Student.get_max_course(self)
        if self.Physics>max:
            max=self.Physics
        if self.Chemistry>max:
            max=self.Chemistry
        if self.History>max:
            max=self.History
        if self.Biology>max:
            max=self.Biology
        if self.Politics>max:
            max=self.Politics
        return max
high_stu=HighSchoolStudent('Lee',20,67,86,76,72,80,94,83,74)
print(high_stu.get_max_course())

