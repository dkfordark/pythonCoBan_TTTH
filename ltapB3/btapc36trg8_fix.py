# 36trg8
def NhapSo():
    so = int(input("Nhap số nguyên (co 4 chu so) : "))
    return so

def ChuSoMax(n):
    chan = le = 0
    while (n>0):
        so = n%10
        if so % 2 ==0:
            chan += 1
        else:
            le += 1
        n = n//10
    return chan, le

def DemChanLe(n):
    chan = le = 0
    while(n>0):
        so = n % 10
        if (so % 2 == 0):
            chan += 1
        else:
            le += 1
        n //= 10
    return chan, le

a, b = DemChanLe(NhapSo())
print("Trong so %d co %d so chan va %d so le"%(NhapSo(),a, b))