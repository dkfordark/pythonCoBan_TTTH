def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def KiemTra(n):
    c = 0
    for i in range(1,n//2):
        if (n%i==0):
            c += 1

    if (c == 2):
        print("%d la so nguyen to"%(n))
    else:
        print("%d ko phai la so nguyen to" % (n))

def KiemTra1a(n):
    c = 0
    for i in range(1,n+1):
        if (n%i==0):
            c += 1

    if (c == 2):
        print("%d la so nguyen to"%(n))
    else:
        print("%d ko phai la so nguyen to" % (n))

KiemTra(NhapSo())

