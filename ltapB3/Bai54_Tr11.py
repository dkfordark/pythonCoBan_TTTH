import math
def NhapSo():
    so = int(input('Nhập số nguyên dương n:'))
    return so
def KiemTraSNT(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
def ThucHien(n):
    for i in range(n - 1, 1, -1):
        if KiemTraSNT(i) :
            print('Số nguyên tố đầu tiên và có giá trị gần nhất với %d là: %d'%(n, i))
            break
n = NhapSo()
ThucHien(n)
