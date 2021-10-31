def NhapSo():
    lst = []
    while True:
        try:
            n = int(input("Vui long nhap so nguyen duong n (kết thúc việc nhập khi nhập số <0): "))
        except Exception:
            print("gia tri ko phai kieu so")
        else:
            if type(n) is not int:
                print("vui long nhap so nguyen duong")
            elif n < 0:
                break
            else:
                #print("them so",n,"vao list")
                lst.append(n)
    return lst
#---------------------------------------------------------
def Dem_x(lst, x):
    if lst.count(x) > 0:
        print('%d xuất hiện %d lần trong lst' % (x, lst.count(x)))
    else:
        print('%d không xuất hiện trong lst' % (x))
#---------------------------------------------------------
def KiemTraX(lst, X):
    if X >= max(lst):
        print('Không có số nào lớn hơn %d' % (X))
    else:
        for i in lst:
            if i > X:
                print(i, end=' ')
#---------------------------------------------------------
def TongKC(lst):
    Tong = 0
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            Tong = Tong + abs(lst[i]-lst[j])
    return Tong
#---------------------------------------------------------
lst = NhapSo()
print(lst)
print("Tổng các số có trong list=",sum(lst))
