#from math import *
import math
print("cau22/p6")
print("pt bac 2: ax\u00b2+bx+c=0")
a,b,c = map(int,input("Moi ban nhap 3 so nguyen a,b,c cach nhau boi dau ,").split(","))
delta = b**2 - 4*a*c
print("Delta: ",delta)
if delta<0:
     print("Ptrinh vo nghiem")
elif delta==0:
     x = -b / 2 * a
     print("Ptrinh co nghiem kep x\u2081 = x\u2082 = ",x)
else:
     x1 = (-b+ math.sqrt(delta)) / (2*a)
     x2 = (-b- math.sqrt(delta)) / (2*a)
     print("Ptrinh co 2 nghiem phan biet")
     print("x\u2081 =",x1)
     print("x\u2082 =",x2)