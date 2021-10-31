import math

def NhapSo():
    lst = []
    while True:
        try:
            n = int(input("Vui long nhap so nguyen duong n: "))
        except Exception:
            print("gia tri ko phai kieu so")
        else:
            if type(n) is not int:
                print("vui long nhap so nguyen duong")
            elif n < 0:
                return False
        return True

lstSo = ["Khong","Mot","Hai","Ba","Tu","Nam","Sau","Bay","Tam","Chin"]

a = n = NhapSo()
k = 0
while (n>0):
    n /= 10
    k += 1
i = pow(10,k-1)

while (a>0):
    k = a / i
    print(k)
    a = a - k*i
    i /= 10




