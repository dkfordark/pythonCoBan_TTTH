import math
from random import *
# a

def ktraSNT(n):
    if (n<=1):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True

def NhapSo():
    while True:
        try:
            n=eval(input("Nhap so nguyen >0: "))
        except Exception:
            print("gia tri nhap khong phai kieu so")
        else:
            if type (n) is not int:
                print("chi nhan so nguyen > 0")
            elif n<=0:
                print("la so nguyen nhung phai > 0")
            else:
                return n

def hamsoMM (k):
    while k>0:
        so = k%10
        if so != 6 and so != 8:
            return False
        k = k // 10
    return True

# a -> b
n = NhapSo()
lst = sample(range(1,10),n)
print(lst)

lst1 = []
for i in lst:
    if ktraSNT(i)==False:
        lst1.append(i)
print("list ko co so nto: ",end='')
print(lst1)

