class Student:
    def __init__(self,name,age,Chinese,Math,English):
        self.name=name
        self.age=age
        self.Chinese=Chinese
        self.Math=Math
        self.English=English
    def get_name(self):
        return self.name
    def get_name(self):
        return self.age
    def get_max_course(self):
        max=self.Chinese
        if self.Math>=self.Chinese:
            max=self.Math
        if self.English>=self.Chinese:
            max=self.English
        return max
stu=Student('zhangsan',18,78,84,62)


