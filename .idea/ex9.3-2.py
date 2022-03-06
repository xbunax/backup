import math
class Round:
    def __init__(self,where,r,color):
        self.where=where
        self.r=r
        self.color=color
    def get_where(self):
        return where
    def get_r(self):
        return r
    def get_color(self):
        return color
    def get_zhouchang(self):
        zhouchang=2*math.pi*self.r
        return zhouchang
    def get_cover(self):
        cover=math.pi*self.r*self.r
        return cover
round=Round('(2,3)',3,'blue')
print(round.get_cover())



