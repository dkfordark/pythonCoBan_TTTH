import math
# --------------------------------
def NhapSo():
    while True:
        try:
            n = int(input("vui long nhap so nguyen: "))
        except Exception:
            print('Gia tri ko phai la kieu so')
        else:
            if type(n) is not int:
                print('Chi nhan so nguyen')
            elif (n<=0):
                print('chi nhan so > 0')
            else:
                return n
# --------------------------------
# c37trg34
def FindNumber(k):
    pre = next = 0
    if (k<=0):
        pre = 0
        next = 1

    for i in range(2,k):
        if (k == 1):
            pre = 0
        else:
            if int(math.sqrt(i))**2==i:
                pre = i
    # print(pre)
    for j in range(1,2*k):
        if int(math.sqrt(j))**2==j:
            next = j
    # print(next)
    return(pre,k,next)
# --------------------------------
lst = [8,-2,5,9]
lst2 = list(map(FindNumber,lst))
print(lst)
print(lst2)
