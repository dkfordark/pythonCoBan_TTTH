# c13trg21
# CauA = lambda n:abs(n)
# n = int(input("nhap so"))
# print("cau A: tri tuyet doi cua %d la %d"%(n,CauA(n)))
#
# CauB = lambda n: n+15
# n = int(input("nhap so"))
# print("cau B: %d + 15 = %d "%(n,CauB(n)))

# CauC = lambda x,y: x * y
# x,y = map(int,input("Nhap x,y: ").split(' '))
# print("CauC: %d * %d = %d"%(x,y,CauC(x,y)))

# CauD = lambda n: print('%d la boi so cua 13 hoac 19'%(n)) if n%13==0 or n%19==0 else print('khong phai boi so')
# n = int(input("moi nhap n:"))
# CauD(n)

# CauD = lambda n: '%d la boi so cua 13 hoac 19'%(n) if n%13==0 or n%19==0 else 'khong phai boi so'
# n = int(input("moi nhap n:"))
# print(CauD(n))

# CauE = lambda r: (3.14*r*r, 2*3.14*r)
# lu = int(input('Nhập bán kính hình tròn: '))
# print('Câu E: Diện tích là: %d và Chu vi là: %d' %(CauE(lu)))

# import math
# CauG = lambda n: '%d la so chinh phuong'%(n) if int(math.sqrt(n))**2==n else 'khong phai so chinh phuong'
# n = int(input('Nhập n: '))
# print(CauG(n))

# CauH = lambda a,b,c: '3 tam giac hop le' if (a+b>c or a+c>b or b+c>a) else '3 canh tam giac ko hop le'
# a,b,c = map(int,input("Nhap 3 canh tam giac: ").split(' '))
# print(CauH(a,b,c))

# Cau16trg22
# def Ktra3Canh(a,b,c):
#     if (a + b > c or a + c > b or b + c > a):
#         return True
#     else:
#         return False
#
# def KtraTamGiac(a,b,c):
#     if (Ktra3Canh(a,b,c)):
#         if(a==b==c):
#             print("Tam giac deu")
#         elif (a==b or a==c or b==c):
#             print("tam giac can")
#         elif (a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2):
#             print("tam giac vuong")
#         else:
#             print("tam giac thuong")
#
# Cau16 = lambda a,b,c: KtraTamGiac(a,b,c)
# a,b,c = map(int,input("Nhap 3 canh tam giac: ").split(' '))
# Cau16(a,b,c)
#
# # c17trg22
# cau_17 = lambda S:S+''

# c34trg33
# lst1=[1,2,3]
# print("List1 = ",lst1)
# resultList=list(map(str,lst1))
# print("Result list=",resultList)

# c35trg33
# import math
# lstB = list(range(10,101,10))
# lstE = list(range(1,11))
# print(lstB)
# print(lstE)
# resultList = list(map(pow,lstB,lstE))
# print(resultList)

# c
def Cong_Tru(a,b):
    return a+b,a-b
lstX = [6,5,3,9]
lstY = [0,1,7,7]
print(lstX)
print(lstY)
resultList = list(map(Cong_Tru,lstX,lstY))
print(resultList)

