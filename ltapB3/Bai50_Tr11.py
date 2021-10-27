import math
def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so
#---------------------
def KiemTra(n):
    c = 0
    for i in range(1,n//2):
        if (n%i==0):
            c += 1
    if (c == 2):
        print("%d la so nguyen to"%(n))
    else:
        print("%d ko phai la so nguyen to" % (n))
#---------------------
def KiemTra2(n):
    if (n<=1):
        return False
    for i in range(2, int(math.sqrt(n))+1 ):
        if (n%i==0):
            return False
    return True

#KiemTra(NhapSo())
n=9876543210987654321098765
if KiemTra2(n)==True:
    print("%d la so nguyen to" % (n))
else:
    print("%d ko phai la so nguyen to" % (n))


