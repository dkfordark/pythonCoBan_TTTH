def NhapSo():
    so=int(input("Nhập số nguyên: "))
    return so
#-----------------
def TongTich(n):
    tong=0
    tich=1
    while n>0:
        so = n%10
        tong=tong+so
        tich=tich*so
        n=n//10
    return tong,tich
#-----------------
n=NhapSo()
tong, tich=TongTich(n)
print ("Tổng các số có trong số %d là %d" %(n,tong))
print ("Tích các số có trong số %d là %d" %(n,tich))