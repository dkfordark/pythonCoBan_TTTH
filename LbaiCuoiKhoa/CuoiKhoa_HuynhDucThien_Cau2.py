# # -----------------------------------------------------
def XoaZero(s):
    s = s.split('.')
    lst = [int(i) for i in s]
    print(lst)
    sSau = ''
    for i in lst:
        sSau = sSau + str(i) + '.'
    return sSau.rstrip('.')
# -----------------------------------------------------
def NhapSo():
    a, b, c, d, e, f = map(eval, input("Vui long nhap 6 so thuc cach nhau boi dau ; :").split(";"))
    return a,b,c,d,e,f
# -----------------------------------------------------
def GiaiHePhuongTrinh(a,b,c,d,e,f):
    x = y = 0
    # a, b, c, d, e, f = map(eval, input("Vui long nhap 6 so thuc: ").split(";"))
    D = a * e - b * d
    Dx = c * e - b * f
    Dy = a * f - d * c
    # print("D:{}\tDx:{}\tDy:{}".format(D, Dx, Dy))
    if (D == Dx == Dy == 0):
        print("\nPtrinh co vo so nghiem")
    elif (D == 0 and (Dx != 0 or Dy != 0)):
        print("Ptrinh vo nghiem")
    elif (D != 0):
        # print("Ptrinh co 1 nghiem")
        x = Dx / D
        y = Dy / D
        # print(("Gia tri x:{} y:{}").format(x, y))
    return x, y
# -----------------------------------------------------
# # --------------- Chuong trinh chinh ------------------
# # ------Cau 2------------------------------------------
# Cau 2a
s = '192.024.001.023'
s = input("Vui long nhap so IP format <xxx.xxx.xxx.xxx> : ")
print('Chuoi sau khi xoa ZeroDu:',XoaZero(s))
# Cau 2b
lstAnSo = [ x for x in NhapSo() ]
print(lstAnSo)
ga, cho = GiaiHePhuongTrinh(lstAnSo[0],lstAnSo[1],lstAnSo[2],lstAnSo[3],lstAnSo[4],lstAnSo[5])
print(f'Co {ga} ga va {cho} cho')

