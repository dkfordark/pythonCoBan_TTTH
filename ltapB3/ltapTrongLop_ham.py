def InBcc(bcc):
    print("bang cuu chuong %d"%bcc)
    for j in range(1,11):
        print("%d x %2d = %5d"%(bcc,j,bcc*j))

def ThucHien(a,b):
    if (a > b):
        a, b = b, a
    for bcc in range (a,b+1):
        InBcc(bcc)
# -----------------------------
a, b = map(int,input("vui long nhap 2 so nguyen: ").split())
ThucHien(a,b)