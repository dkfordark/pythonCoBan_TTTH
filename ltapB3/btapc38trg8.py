def NhapSo():
    so = int(input("Moi nhap số nguyên: "))
    return so

def KiemTra(n):
    kt, chan, le = 0,0,0
    n = abs(n)
    while n > 0:
        kt = n % 10
        if (kt % 2 == 0):
            chan += 1
        else:
            le += 1
        n //= 10
    return chan, le

chan, le = KiemTra(NhapSo())
if (chan == 0):
    print("So nhap toan le")
elif (le == 0):
    print("So nhap toan chan")
else:
    print("So nhap co chan va le")