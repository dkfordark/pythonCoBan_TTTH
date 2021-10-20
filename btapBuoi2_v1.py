# from math import *
# print("cau22/p6")
# print("pt bac 2: ax\u00b2+bx+c=0")
# a,b,c = map(int,input("Moi ban nhap 3 so nguyen a,b,c cach nhau boi dau ,").split(","))
# delta = b**2 - 4*a*c
# print("Delta: ",delta)
# if delta<0:
#     print("Ptrinh vo nghiem")
# elif delta==0:
#     x = -b / 2 * a
#     print("Ptrinh co nghiem kep x\u2081 = x\u2082 = ",x)
# else:
#     x1 = (-b+sqrt(delta)) / (2*a)
#     x2 = (-b-sqrt(delta)) / (2*a)
#     print("Ptrinh co 2 nghiem phan biet")
#     print("x\u2081 =",x1)
#     print("x\u2082 =",x2)

# print("Cau23/p6")
# print("Nhap toa do 3 dinh cua 1 tam giac")
# xA, yA = map(eval,input("Nhap toa do x y cua diem A").split(" "))
# xB, yB = map(eval,input("Nhap toa do x y cua diem B").split(" "))
# xC, yC = map(eval,input("Nhap toa do x y cua diem C").split(" "))
# print("Nhap toa do diem P")
# xP, yP = map(eval,input("Nhap toa do x y cua diem P").split(" "))
# z1 = (xB-xA) * (yP-yA) - (yB-yA) * (xP-xA)
# z2 = (xC-xB) * (yP-yB) - (yC-yB) * (xP-xB)
# z3 = (xA-xC) * (yP-yC) - (yA-yC) * (xP-xC)
# if((z1>0 and z2>0 and z3>0) or (z1<0 and z2<0 and z3<0)):
#     print("Diem P nam trong tam giac")
# else:
#     print("Diem P nam ngoai tam giac")

# print("Cau24/p6")
# x1, y1, r1 = map(int,input("vui long nhap x, y va r cho vong tron C1: ").split(","))
# x2, y2, r2 = map(int,input("vui long nhap x, y va r cho vong tron C2: ").split(","))
# c1c2 = ((x2-x1)**2 + (y2-y1)**2)**0.5
# if(c1c2 <= r2):
#     print("C1 nam trong C2")
# elif(c1c2 <= r1):
#     print("C2 nam trong C1")
# elif(c1c2>abs(r2-r1) and c1c2<(r2+r1)):
#     print("C1, C2 cat nhau")
# elif(c1c2 > r1+r2):
#     print("C1, C2 khong cat nhau")

# print("Bai25")
# a, b, c, d, e, f = map(eval, input("Vui long nhap 6 so thuc: ").split(";"))
# D = a * e - b * d
# Dx = c * e - b * f
# Dy = a * f - d * c
# print("D:{}\tDx:{}\tDy:{}".format(D, Dx, Dy))
# if (D == Dx == Dy == 0):
#     print("Ptrinh co vo so nghiem")
# elif (D == 0 and (Dx != 0 or Dy != 0)):
#     print("Ptrinh vo nghiem")
# elif (D != 0):
#     print("Ptrinh co 1 nghiem")
#     x = Dx / D
#     y = Dy / D
#     print(("Gia tri x:{} y:{}").format(x, y))

# print("Bai29/trg7")
# n = int(input("vui long nhap n: "))
# a = int(input("vui long nhap so hang dau tien: "))
# p = int(input("vui long nhap cong boi: "))
# if(n>0):
#     i=0
#     print("Cac so hang: ")
#     while(i<n):
#         i+=1
#         a*=p
#         print(a,end=" ")

