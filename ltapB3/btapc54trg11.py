import math
def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def KtraSo(n):
    for i in range (n-1,1,-1):
        if KtraSNT(i):
            print("So nto co gia tri gan nhat: ",i)
            break

def KtraSNT(n):
    if (n<=1):
        return False
    for i in range(2,int(math.sqrt(n+1)) + 1):
        if (n%i==0):
            return False
    return True

n = NhapSo()
KtraSo(n)

