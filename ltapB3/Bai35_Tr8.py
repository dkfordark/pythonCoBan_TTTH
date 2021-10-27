def NhapSo():
    so = int(input("Nhap số nguyên: "))
    return so

def ChuSoMax(n):
    lon=0
    while n>0:
        so=n%10
        if so>lon:
            lon=so
        n=n//10
    return lon

a = ChuSoMax(NhapSo()) # vi du 5084
print("Chu so lon nhat la", a)