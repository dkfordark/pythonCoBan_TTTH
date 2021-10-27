def NhapSo():
    so = int(input("Nhap số nguyên: "))
    return so
#----------------
def CauF(n):    #S= 1 + (1+2) + (1+2+3)
    t1, t2 = 0, 0
    for i in range(1,n+1):
        t1 += i
        t2 += t1
    return t2
#----------------
def CauH(n):
    t1, t2 = 1, 1
    for i in range(1,n+1):
        t1 *= i
        t2 *= t1
    return t2
#----------------
def CauG(n):
    tich = 1
    for i in range(1,n+1):
        tich *= (2*i-1)
    return tich
#----------------   CHƯƠNG TRÌNH CHÍNH  -----------------
n=NhapSo()
print('Kết quả câu F= {}'.format(CauF(n)))
print('Kết quả câu G= {}'.format(CauG(n)))
print('Kết quả câu H= {}'.format(CauH(n)))
