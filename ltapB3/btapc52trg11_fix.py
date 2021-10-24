import math
def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def UocSo(n):
    print("cac uoc so nguyen to cua %d la:"%n)
    for i in range(2,n//2):
        if n % i == 0 and KiemTra2(i)==True:
            print(i,end=" ")

def KiemTra2(n):
    if (n<=1):
        return False
    for i in range(2,int(math.sqrt(n+1)) + 1):
        if (n%i==0):
            return False
    return True

n = NhapSo()
UocSo(n)

