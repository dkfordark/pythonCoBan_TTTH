import math
def integer():
    n=int(input("nhap so nguyen :"))
    return n
#--------------------------------------
def isprime(n):
    if n<=1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# --------------------------------------
def ThucHien(n):
    print("Các ước số  nguyên tố của %d là: " %n)
    for i in range (2,n//2):
        if n%i==0 and isprime(i)==True:
            print(i,end=" ")
#--------------------------------------
a=integer()
ThucHien(a)
