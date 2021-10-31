import random, math
def NhapSo():
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
#-------------------------
def Taolst(n):
    '''lst = []
    for i in range(n):
        lst.append(random.randint(0, 1001))'''
    return random.sample(range (1,10000), n)
#----------------------------
def CauC(lst):
    print("Cau C: cac cho chan:", end='')
    for i in lst:
        if i%2 == 0:
            print(i," ",end='')
        if i==99:
            print("99")
            break
#---------------------------
def LaSoMayMan(k):
    while k>0:
        so=k%10
        if so !=6 and so !=8:
            return False
        k=k//10
    return True
#---------------------------
def LaSoMayMan(k):
    if k<=0:
        return False
    while k>0:
        so=k%10
        if so !=6 and so !=8:
            return False
        k=k//10
    return True
def CauD(lst):
    dem=0
    for i in lst:
        if LaSoMayMan(i):
            if dem==0:
                print("\nCác số may mắn có trong list là: ", end=" ")
            print("%5d"%i, end=" ")
            dem+=1
    if dem==0:
        print("\nTrong list không có số may mắn")
#-----------------------
def ktraSNT(n):
    if (n<=1):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True
#-----------------------
def CauE(lst):
    dem=0
    for i in lst:
        if ktraSNT(i):
            if dem==0:
                print("\nCác số nguyên tố có trong list là: ", end=" ")
            print("%5d"%i, end=" ")
            dem+=1
    if dem==0:
        print("\nTrong list không có số nguyên tố")
#-----------------------    chương trình chính  -------------------
n=NhapSo()
lst=Taolst(n)
print("List ban dau:", lst)
CauC(lst)
CauD(lst)
CauE(lst)