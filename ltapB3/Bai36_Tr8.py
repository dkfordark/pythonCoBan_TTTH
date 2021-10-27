def NhapSo():
    so = int(input("Nhap số nguyên: "))
    return so

def DemChanLe(n):
    chan=le=0
    while n>0:
        so=n%10
        if so%2==0:
            chan+=1
        else:
            le+=1
        n=n//10
    return chan, le

n=NhapSo()
chan, le=DemChanLe(n)
print("Trong so {} co {} so chan va {} so le".format(n,chan, le))