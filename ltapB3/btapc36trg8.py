# 36trg8
def NhapSo():
    so = int(input("Nhap số nguyên (co 4 chu so) : "))
    return so

def ChuSoMax(n):
    a = n%10 # => 4
    n //= 10
    b = n%10 # => 8
    n //= 10
    c = n%10 # => 0
    n //= 10
    d = n%10 # => 5
    # print(f"4 so {a} {b} {c} {d}")
    # print("so lon nhat la: %d"%(max(a,b,c,d)))
    return (max(a,b,c,d))

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

# a = ChuSoMax(NhapSo()) # vi du 5084
# print("Chu so lon nhat la", a)

a, b = DemChanLe(NhapSo())
print("Co %d so chan va %d so le"%(a, b))