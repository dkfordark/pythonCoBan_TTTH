import math

def TongKC(lst):
    Tong = 0
    for i in range(0, len(lst)-1):
        for j in range(i+1, len(lst)):
            Tong = Tong + abs(lst[i]-lst[j])
    return Tong

def NhapSo():
    lst = []
    while True:
        try:
            n = int(input("Vui long nhap so nguyen duong n: "))
        except Exception:
            print("gia tri ko phai kieu so")
        else:
            if type(n) is not int:
                print("vui long nhap so nguyen duong")
            elif n < 0:
                break
            else:
                print("them so",n,"vao list")
                lst.append(n)
    return lst

# a
# lst = NhapSo()
# print("List duoc tao:",lst)

# b
# tong = 0
# for i in lst:
#     tong += i
# print("Tong cac so trong list: ", tong)
# print("Tong cac so trong list: ", sum(lst))

# c
# lst = NhapSo()
# print("List duoc tao:",lst)
# x = int(input("Vui long nhap so nguyen x: "))
# count = 0
# for i in lst:
#     if i == x:
#         count += 1
# print("so lan xuat hien cua %d: %d lan"%(x,count))

# d
# lst = NhapSo()
# print("List duoc tao:",lst)
# x = int(input("Vui long nhap so nguyen x: "))
# max = max(lst)
# print(max)
# if (x > max):
#     print ("%d la lon nhat",x)
# else:
#     print("So lon hon x:",end='')
#     for i in lst:
#         if i > x:
#             print("%d "%i,end='')

# e
# lst = NhapSo()
# print("List duoc tao:",lst)
# print("Tong khoang cach giua cac so trong list:",TongKC(lst))

