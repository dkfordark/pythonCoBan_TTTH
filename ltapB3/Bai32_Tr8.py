from MyLib import ThucHien
def InBCC(bcc): # bcc là parameter
    print("bang cuu chuong %d" % bcc)
    for i in range(1, 11):
        print("%d X %2d = %5d" % (bcc, i, bcc * i))
#====================================================
def ThucHien(a,b):
    if a > b:
        a, b = b, a
    for bcc in range(a, b + 1):
        InBCC(bcc)
#====================================================
def Nhap2So():
    a, b = map(int, input("Nhập 2 số nguyên: ").split())
    return a,b
#-------------------      CHƯƠNG TRÌNH CHÍNH    --------------------
ThucHien(Nhap2So())




'''a, b = map(int, input("Nhập 2 số nguyên: ").split())
print("Su dung WHILE de in bang cuu chuong")
bcc=a
while bcc<b:
    print("bang cuu chuong %d" %bcc)
    i=1
    while i<=10:
        print( "%d X %2d = %3d" %(bcc, i,bcc*i))
        i+=1
    bcc+=1
'''