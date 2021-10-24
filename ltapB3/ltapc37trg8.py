def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def TachSo(n):
    n = abs(n)
    while(n>0):
        if (n!=8 and n!=6):
            return False
        n //= 10
    return True

n = NhapSo()
TachSo(n)
if TachSo(n) == True:
    print("n la so may man")
else:
    print("n ko phai la so may man")