# 35trg8_fix
def NhapSo():
    so = int(input("Nhap số nguyên (co 4 chu so) : "))
    return so

def ChuSoMax(n):
    lon=0
    while n>0:
        so= n % 10
        if so > lon:
            lon = so
        n //= 10
    return lon

a = ChuSoMax(NhapSo())
print("Chu so lon nhat la", a)
