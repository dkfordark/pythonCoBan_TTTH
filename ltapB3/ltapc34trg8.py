def NhapSo():
    so = int(input("Nhap số nguyên : "))
    return so

def TongTich(n):
    tong = 0
    tich = 1
    while (n>0):
        so = n%10
        tong += so
        tich *= so
        n //=10
    return tong, tich

n = NhapSo()
tong, tich = TongTich(n)
print("Tong cac so trong %d la %d"%(n,tong))
print("Tich cac so trong %d la %d"%(n,tich))