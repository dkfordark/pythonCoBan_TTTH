def nhapso():
    try:
        n = int(input("moi nhap so nguyen duong n: "))
    except Exception:
        print("Vui long nhap so")
    else:
        if (n<0):
            print("vui long nhap so > 0")
        elif type(n) is not int:
            print("day khong phai so nguyen")
        else:
            return n
# -----------------------------------------------------
def numDecr(lst):
    temp = 0
    for i in range(0, len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst
# -----------------------------------------------------
def numIncr(lst):
    temp = 0
    for i in range(0, len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst
# -----------------------------------------------------
def tachSo(n):
    lst = []
    while (n > 0):
        lst.append(n % 10)
        n //= 10
    return lst
# -----------------------------------------------------
def disp(lst):
    for i in lst:
        print(i,end='')
    print("\n")
# -----------------------------------------------------
def combine(lst):
    t = 0;
    for i in lst:
        t = (t + i)*10
    return int(t/10)
# --------------- chuong trinh chinh ------------------
n = nhapso()
lst = tachSo(n)
lstIncr=numIncr(lst.copy())
lstDecr=numDecr(lst.copy())
# disp(lstIncr) # xuat mang tang
# disp(lstDecr) # xuat mang giam
nMin=combine(lstIncr)
nMax=combine(lstDecr)
print("So min %d"%(nMin))
print("So max %d"%(nMax))
print("nMax - nMin = %d - %d = %d"%(nMax,nMin,nMax-nMin))