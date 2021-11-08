# c87trg46
# lst1 = [1,2,3,9]
# lst2 = [4,8,6,12]
# lst3 = [7,5,10,11]
# lst4 = list(map(lambda x,y,z : max(x,y,z),lst1,lst2,lst3))
# print(lst4)

# c88trg46
# Cau A
# lst1 = [-5,10,-3,-1,7,8,9,2]
# lstChan = list(filter(lambda x : x % 2==0, lst1))
# print("List chan: ",lstChan)
# lstLe = list(filter(lambda x : x % 2!=0, lst1))
# print("List le: ",lstLe)

# Cau B
# lst1 = [-5,10,-3,-1,7,8,9,2]
# lstChan = list(filter(lambda x : x % 2==0, lst1))
# print("Luong so chan: ",len(lstChan))
# lstLe = list(filter(lambda x : x % 2!=0, lst1))
# print("Luong so le: ",len(lstLe))

# Cau C
# lst1 = [-5,10,-3,-1,7,8,9,2]
# lst2 = list(map(lambda x : x**2,lst1))
# lst3 = list(map(lambda x : x**3,lst1))
# print("List binh phuong:",lst2)
# print("List luy thua 3:",lst3)

# Cau D
# import math
# def KtraSNT(n):
#     if (n<=1):
#         return False
#     else:
#         return int(math.sqrt(n))+1
# # --------------------------------
# def SchinhPhuong(n):
#     if (n<1):
#         return False
#     return (int(math.sqrt(n)) ** 2 == n)
# # --------------------------------
# # lst1 = [-5,10,-3,-1,7,8,9,2]
# # # lst1 = [19,65,81,39,152,639,121,44,100,31]
# # lst2 = list(filter(lambda x : SchinhPhuong(x) and KtraSNT(x),lst1))
# # print(lst2)
#
# # c91trg47
# # Câu a
# # lst1 = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
# # lst2 = list(filter(lambda x: len(x)==6,lst1))
# # print(lst2)
# # cau b
# lst1 = ['php','www','Python','abba','Java','MADAM']
# lst2 = list(filter(lambda x: x == x[::-1] ,lst1))
# print(lst2)

# c97trg48
# n = int(input("vui long nhap n: "))
# lst = [x for x in range(1,n+1) if n%x==0]
# print(lst)

# c98trg48
# a
# lst = [int(input("Vui long nhap n: ")) for i in range(8)]
# print(lst)
# b
# import math
# # ------------------------------------------
# def KtrSNT(n):
#     if (n<=1):
#         return False
#     for i in range (2,int(math.sqrt(n))+1):
#         if (n%i==0):
#             return False
#     return True
# # ------------------------------------------
# lst = [ i for i in range (1,9) if KtrSNT(i)]
# print(lst)

# c101trg49
# a
# import random
# n = int(input("Vui long nhap so n : "))
# lstL = [random.randint(0,20) for n in range(n)]
# print(lstL)
# k = int(input("Vui long nhap so k : "))
# lst2 = all(k > i for i in lstL)
# lst3 = any(k > i for i in lstL)
# if (lst2):
#     print("%d lon hon tat ca cac so"%k)
# elif (lst3):
#     print("co so nho hon %d trong list" % k)
# else:
#     print("ko co so nao trong list nho hon %d" % k)
# # b
# lst = [727,6,1421,626,3706,101,3553,4234,33,971]
# lst2 = [ i for i in lst if i < int(str(i)[::-1])]
# print(lst2)

# lst1 = [1,2,3]
# lst2 = [5,10,15,20]
# # lst3 = [x*y for x in ls1 for y in lst2]
# lstC = [x*y for x in lst1 for y in lst2 if (x*y)%2!=0]

# c129trg52
# import random
# n= int(input("Vui long nhap so n : "))
# lst = [random.randint(-100,100) for n in range(n)]
# print((lst))
# lstM = list(filter(lambda x: x>0 ,lst))
# print((lstM))

# c132a_trg52
lstA = [1,1,2,3,5,8,13,21,34,55,89]
lstB = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print("List A: ",lstA)
print("List B: ",lstB)
lstAinB = [ x for x in lstA if x in lstB]
print("List A in B",lstAinB)
lstBinA = [ y for y in lstB if y in lstA]
print("List B in A",lstBinA)