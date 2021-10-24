import math
def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def UocSo(n):
    for i in range(1,n+1):
        if n % i == 0:
            # print("Co uoc so: %d"%(i))
            j = KiemTra2(i)
            if j:
                print("%d la uoc so nguyen to" % (i))

def KiemTra2(n):
    if (n<=1):
        return False
    for i in range(2,int(math.sqrt(n+1)) + 1):
        if (n%i==0):
            return False
    return True

n = NhapSo()
UocSo(n)

