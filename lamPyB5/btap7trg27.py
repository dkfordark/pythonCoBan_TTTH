import math
import random

def lstSoMayMan(lst):
    lst1 = []
    for i in lst:
        if soMayMan(i):
            lst1.append(i)
    return lst1
#---------------------------------
def soMayMan(k):
    while k > 0:
        so = k % 10
        if so != 8 and so != 6:
            return False
        k //= 10
    return True
#---------------------------------
def lstCP(lst):
    lst1 = []
    dem = 0
    for i in lst:
        if int(math.sqrt(i))**2 == i:
            lst1.append(i)
            dem += 1
    if dem == 0:
        print("khong co so chinh phuong nao trong list")
    return lst1
#---------------------------------
def lstSNT(lst):
    lst1 = []
    dem = 0
    for i in lst:
        if ktraSNT(i):
            # if dem == 0:
                # print("cac so nt trong la: ", end='')
            # print("%5d" % i, end='')
            dem += 1
            lst1.append(i)
    if dem == 0:
        print("\nTrong list khong co so nguyen to")
    return (lst1)
#---------------------------------
def ktraSNT(n):
    if n<=1:
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
#---------------------------------
def NhapSo50100():
    while True:
        try:
            n = eval(input('Nhập số nguyên >0 (tu 50 -> 100):'))
        except Exception:
            print('Giá trị không phải kiểu số')
        else:
            if type(n) is not int:
                print('Chỉ nhận số nguyên >0')
            elif n <= 0:
                print('Là số nguyên nhưng phải >0')
            elif n < 50 or n > 100:
                print('Phai nhap so tu 50 -> 100')
            else:
                return n
#---------------------------------
def NhapSoNguyen():
    while True:
        try:
            n = eval(input('Nhập số nguyên >0:'))
        except Exception:
            print('Giá trị không phải kiểu số')
        else:
            if type(n) is not int:
                print('Chỉ nhận số nguyên >0')
            elif n <= 0:
                print('Là số nguyên nhưng phải >0')
            else:
                return n
#---------------------------------

# a
# n = NhapSo50100()
# print(n)

# b
# n = NhapSoNguyen()
# lst = random.sample(range(0,2*n),n)
# print(lst)

# c
# n = NhapSoNguyen()
# lst = random.sample(range(0,2*n),n)
# print("\nList chua cac so nguyen to: ",lstSNT(lst))

# d
# n = NhapSoNguyen()
# lst = random.sample(range(1,2*n),n)
# print("List ban dau:",lst)
# print("\nList chua cac so chinh phuong: ",lstCP(lst))

# e
# n = NhapSoNguyen()
# lst = random.sample(range(1,2*n),n)
# print("List ban dau:",lst)
# lst1 = lstSoMayMan(lst)
# if len(lst1) == 0:
#     print("khong co so may man trong list")
# else:
#     print("List chua cac so may man:",lst1)

# f
# n = NhapSoNguyen()
# lst = random.sample(range(0,2*n),n)
# print("List ban dau:",lst)
# print("List chua cac so nguyen to: ",lstSNT(lst))
# for i in lstSNT(lst):
#     vitri = lst.index(i)
#     del lst[vitri]
# print("List sau khi xoa so nguyen to: ",lst)

# g
# n = NhapSoNguyen()
# lst = random.sample(range(1,2*n),n)
# print("List ban dau:",lst)
# print("List chua cac so chinh phuong: ",lstCP(lst))
# for i in lstCP(lst):
#     vitri = lst.index(i)
#     del lst[vitri]
# print("List sau khi xoa so chinh phuong: ",lst)