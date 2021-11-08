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
# --------------------------------------------
def ChkTu(chuoi):
    ch_dau = []
    dem = 0
    for i in range(0,len(chuoi)-1):
        for j in range(i+1,len(chuoi)):
            if chuoi[i] != chuoi[j]:
                dem = 1
                ch_dau.append((chuoi[j]).lower())
    return ch_dau
# --------------------------------------------
# lst = list(input('Vui long nhap ten cach nhau boi dau phay:').split(','))
lst = ['Red','Blue','Black','White','Pink']
print(lst)
GomLst = "".join(lst)
print(GomLst)
print(len(GomLst))
print(sorted(ChkTu(GomLst)))