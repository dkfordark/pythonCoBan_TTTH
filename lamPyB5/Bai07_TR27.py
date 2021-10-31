import math, random
def CauA():
    while True:
        try:
            n=int(input("Nhập số nguyên từ 50-100:"))
        except Exception:
            print("Giá trị vừa nhập không phải là số nguyên. Yêu cầu nhập lại")
        else:
            if n<50 or n>100:
                print("Chỉ nhận giá trị từ 50-100. Yêu cầu nhập lại")
            else:
                return n
#-------------------
def CauB(n):
    lst=[]
    for i in range (n):
        lst.append(random.randint(0,2*n))
    return lst
#-----------------------
def ktraSNT(n):
    if (n<=1):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True
#-----------------------
def CauC(lst):
    dem=0
    for i in lst:
        if ktraSNT(i):
            if dem==0:
                print("Các số nguyên tố có trong list")
            print("%5d"%i,end=" ")
            dem+=1
    if dem==0:
        print("Trong list không chứa số nguyên tố")
# -------------------
def LaSoCP(n):
    if int(math.sqrt(n))**2==n:
        return True
    else:
        return False
#-----------------------
def CauD(lst):
    dem=0
    for i in lst:
        if LaSoCP(i):
            if dem==0:
                print("Các số chính phương có trong list")
            print("%5d"%i,end=" ")
            dem+=1
    if dem==0:
        print("Trong list không chứa số chính phương")
# --------------------
def LaSoMayMan(n):
    if n<6:
        return False
    while n>0:
        so=n%10
        if so !=6 and so !=8:
            return False
        n=n//10
    return True
#-----------------------
def CauE(lst):
    dem=0
    for i in lst:
        if LaSoMayMan(i):
            if dem==0:
                print("Các số may mắn có trong list")
            print("%5d"%i,end=" ")
            dem+=1
    if dem==0:
        print("Trong list không chứa số may mắn")
#-----------------------
def CauF(lst):
    dem=0
    for i in range(len(lst)-1,-1,-1): # 0-> len(lst)-1
        if ktraSNT(lst[i]):
            lst.remove(lst[i])
    return lst
#-----------------------
def CauG(lst):
    dem=0
    for i in range(len(lst)-1,-1,-1): # 0-> len(lst)-1
        if LaSoCP(lst[i]):
            lst.remove(lst[i])
    return lst
#-----------------------
n=CauA()
lst=CauB(n)
print("List ban đầu:",lst)
CauC(lst)
CauD(lst)
CauE(lst)
#lst1=CauF(lst)
print("\nList sau khi xóa số nguyên tố:",len(CauF(lst.copy())))
print("List ban đầu:",len(lst))
#lst2=CauG(lst)
#print("List sau khi xóa số chính phương:",lst2)
x=5


