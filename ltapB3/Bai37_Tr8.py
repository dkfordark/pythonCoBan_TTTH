def NhapSo():
    so = int(input('Nhập số nguyên n:'))
    return so
#--------------------------------------------
def Kiemtra(n):
    n = abs(n)
    while n > 0:
        if n % 10 != 6 and n % 10 != 8:
            return False
        n = n // 10
    return True
#--------------------------------------------
n = NhapSo()
if Kiemtra(n)==True:
    print('n là số may mắn')
else:
    print('n không phải là số may mắn')

