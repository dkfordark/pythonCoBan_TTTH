# def Chon(c):
#     print("0. Nhap canh tam giac: ")
#     print("1. Tam giac 1 ")
#     print("2. Tam giac 2 ")
#     print("3. Tam giac 3 ")
#     print("4. Tam giac 4 ")
#     print("5. Tam giac 5 ")
#     print("6. Tam giac 6 ")
#     print("7. Tam giac 7 ")
#     print("8. Tam giac 8 ")
#     print("9. Ket thuc chuong trinh")
#     c = int(input("Moi chon "))
#     return c

def NhapSo():
    so = int(input("Nhap canh tam giac vuong: "))
    return so

def VeHinh01(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong+cot<=n+1):
                print("* ", end="")
            else:
                print(" ", end="")
        print()

def VeHinh02(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong+cot>=n+1):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh03(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==1 or cot==1 or dong+cot==n+1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh04(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==n or cot==n or dong+cot==n+1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh05(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong-cot <= 0):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh06(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong-cot >= 0):
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh07(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==n or cot==1 or dong==cot:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def VeHinh08(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==1 or cot==n or dong==cot:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def menu():
    n = 0
    while True:
        print("chuong trinh tam giac vuong can")
        print("0. Nhap canh tam giac: ")
        print("1. Tam giac 1 ")
        print("2. Tam giac 2 ")
        print("3. Tam giac 3 ")
        print("4. Tam giac 4 ")
        print("5. Tam giac 5 ")
        print("6. Tam giac 6 ")
        print("7. Tam giac 7 ")
        # print("8. Tam giac 8 ")
        print("9. Ket thuc chuong trinh")
        print("Ban chon ?: ")
        chon = int(input("Moi chon "))

        if chon == 0:
            n = NhapSo()
        elif chon == 1:
            VeHinh01(n)
        elif chon == 2:
            VeHinh02(n)
        elif chon == 3:
            VeHinh03(n)
        elif chon == 4:
            VeHinh04(n)
        elif chon == 5:
            VeHinh05(n)
        elif chon == 6:
            VeHinh06(n)
        elif chon == 7:
            VeHinh07(n)
        elif chon == 8:
            VeHinh08(n)
        elif chon == 9:
            print("Bye bye")
            break
        else:
            print("chuong trinh chi nhan so tu 0-9. Yeu cau nhap lai.")

# --------- chuong trinh chinh
menu()
n = NhapSo()
VeHinh01(n)
VeHinh02(n)
VeHinh03(n)
VeHinh04(n)
VeHinh05(n)
VeHinh06(n)
VeHinh07(n)
VeHinh08(n)

