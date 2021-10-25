import math
def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def KiemTra2(n):
    if (n<=1):
        return False
    for i in range(2,int(math.sqrt(n+1)) + 1):
        if (n%i==0):
            return False
    return True

n = NhapSo()
if KiemTra2(n):
    print("%d la so nguyen to" % (n))
else:
    print("%d ko phai la so nguyen to" % (n))
