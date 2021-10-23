def NhapSo():
    so = int(input("Nhap so n: "))
    return so

def CauH(n):
    t1, t2 = 1, 1
    for i in range(1,n+1):
        t1 *= i
        t2 *= t1
    return t2

def CauG(n):
    tich = 1
    for i in range(1,n+1):
        tich *= (2*i-1)
    return tich

def CauF(n):
    t1, t2 = 0, 0
    for i in range(1,n+1):
        t1 += i
        t2 += t1
    return t2

def CauE(n):
    tong = 0
    for i in range(1,n+1):
        tong = tong + 1/(2*i)
    return tong

def CauD(n):
    tong = 0
    for i in range(1,n+1):
        tong = tong + 1/(i+1)
    return tong

def CauC(n):
    tong = 0
    for i in range(1,n):
        tong = tong + 1/i
    return tong

def CauB(n):
    tong = 0
    for i in range(0,n+1):
        tong = tong + (2*i+1)
    return tong

def CauA(n):
    tong = 0
    for i in range(1,n+1):
        tong = tong + i
    return tong

n = NhapSo()
# ketqua = CauA(n)
# print("Kq CauA: ",ketqua)
# ketqua = CauB(n)
# print("Kq CauB: ",ketqua)
# ketqua = CauC(n)
# print("Kq CauC: ",ketqua)
# ketqua = CauD(n)
# print("Kq CauD: ",ketqua)
# ketqua = CauE(n)
# print("Kq CauE: ",ketqua)
# ketqua = CauF(n)
# print("Kq CauF: ",ketqua)
# ketqua = CauG(n)
# print("Kq CauF: ",ketqua)
ketqua = CauH(n)
print("Kq CauF: ",ketqua)