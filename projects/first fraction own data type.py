class Fraction:
   
    def __init__(self,n,d):
        self.num=n
        self.den=d
    
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        temp_num= self.num*other.den +other.num*self.den
        tem_den=self.den *other.den
        return "{}/{}".format(temp_num,tem_den)
x=Fraction(2,4)
y=Fraction(3,2)
print(x)
print(y)
print(x+y)
