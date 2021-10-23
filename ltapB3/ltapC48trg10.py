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

# --------- chuong trinh chinh
n = NhapSo()
VeHinh01(n)
VeHinh02(n)
VeHinh05(n)
VeHinh06(n)

