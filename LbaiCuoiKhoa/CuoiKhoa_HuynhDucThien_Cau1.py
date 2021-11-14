import random
import math
# ----------------------------------------------------------------
def NhapSo():
    while True:
        try:
            n = int(input("Vui long nhap so luong so nguyen duong: "))
        except Exception:
            print('Gia tri nhap khong phai kieu so')
        else:
            if type (n) is not int:
                print('Phai nhap kieu so nguyen. Yeu cau nhap lai')
            elif n < 0:
                print('Phai nhap so nguyen duong. Yeu cau nhap lai')
            elif n < 10 or n > 1000:
                print('Phai nam trong khoang tu 10->1000. Yeu cau nhap lai')
            else:
                return n
# ----------------------------------------------------------------
def TaoLst(n):
    return random.sample(range(1,5001),n)
    # Hang sau de test cau b
    # return random.sample(range(1,100),n)
    # Hang sau de test cau d
    # return random.sample(range(1, 500), n)
# ----------------------------------------------------------------
def TimUSCLN(a, b):
    if (b == 0):
        return a;
    return TimUSCLN(b, a % b);
# ----------------------------------------------------------------
def DaoSo(so):
    soDao = 0
    while so != 0:
        soDao = soDao * 10 + (so % 10)
        so //= 10
    return soDao
# ----------------------------------------------------------------
def KtraLstThanThien(lstSo):
    LstSoThanThien = []
    dem = 0
    for i in lstSo:
        if TimUSCLN(i, DaoSo(i)) == 1:
            dem += 1
            LstSoThanThien.append(i)

    if dem == 0:
        print('Khong co so than thien trong List da tao')
    else:
        print('Cac so than thien trong List la:',end='')
        for j in LstSoThanThien:
            print(" ",j,end='')
# ----------------------------------------------------------------
def KtraSoNguyenTo(so):
    if so < 1:
        return False
    for i in range (2,int(math.sqrt(so))+1):
        if so % i == 0:
            return False
    return True
# ----------------------------------------------------------------
def KtraSNTstrobogrammatic(lstSo):
    dem = 0
    LstSNTstrobo = []
    for i in lstSo:
        if KtraSoNguyenTo(i) and (i == DaoSo(i)):
            dem += 1
            LstSNTstrobo.append(i)

    if dem==0:
        print('\nTrong list khong co so nguyen to strobogrammatic')
    else:
        print('\nCac so nguyen to strobogrammatic trong list la:',end='')
        for j in LstSNTstrobo:
            print(" ",j,end='')
# ----------------------------------------------------------------
def SoMayMan(so,DemLap):
    # SoTam = 0
    # while so != 0:
    #     SoTam = SoTam + (so % 10) ** 2
    #     so //= 10
    # return SoTam

    DemLap += 1
    if DemLap>=100:
        # print('Day ko phai so MM')
        return False

    SoTam = 0
    while so != 0:
        SoTam = SoTam + (so % 10) ** 2
        so //= 10

    if SoTam>1:
        return SoMayMan(SoTam,DemLap)
    elif SoTam==1:
        # print('Day la so MM')
        return True
# ----------------------------------------------------------------
def KiemTraLstSoMayMan(lst):
    dem = 0
    LstSoMayMan = []
    for i in lst:
        if SoMayMan(i,0):
            dem += 1
            LstSoMayMan.append(i)

    if dem == 0:
        print('\nTrong list khong chua so may man')
    else:
        print('\nCac so may man trong list la:',end='')
        for j in LstSoMayMan:
            print(' ',j,end='')
# ----------------------------------------------------------------
# ----------------Chuong trinh chinh---------------------------------
# ----Cau 1----------------------------------------------------------
print('Cau 1')
# Cau 1a
n = NhapSo()
print('So luong so nguyen duong da nhap:',n)
lstSo = sorted(TaoLst(n))
print('List duoc tao:',lstSo)
# Cau 1b
KtraLstThanThien(lstSo)
# Cau 1c
KtraSNTstrobogrammatic(lstSo)
# Cau 1d
KiemTraLstSoMayMan(lstSo)