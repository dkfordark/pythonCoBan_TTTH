#Bài tập về nhà: 61,62,63 trang 13;  49 trang 11
def Hinh09(n):
    print("Hình 09:")
    for dong in range (1,n+1):
        for cot in range (2*n):
            if dong+cot>=n+1 and cot-dong<=n-1:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()

#----------------------------------
def Hinh10(n):
    print("Hình 10:")
    for dong in range (1,n+1):
        for cot in range (2*n):
            if dong<=cot and cot+dong<=2*n:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#-------------------------------------
def Hinh11(n):
    print("Hình 11:")
    for dong in range (1,n+1):
        for cot in range (1,2*n):
            if dong+cot==n+1 or cot-dong==n-1 or dong==n:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#----------------------------------
def Hinh12(n):
    print("Hình 12:")
    for dong in range (1,n+1):
        for cot in range (1,2*n):
            if dong==cot or cot+dong==2*n or dong==1:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#-----------------------------------
def Hinh13(n):
    print("Hình 13:")
    for dong in range (1,2*n):
        for cot in range (1,n+1):
            if dong==cot or cot+dong==2*n or cot==1:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#-----------------------------------
def Hinh14(n):
    print("Hình 14:")
    for dong in range (1,2*n):
        for cot in range (1,n+1):
            if dong+cot==n+1 or dong-cot==n-1 or cot==n:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#-----------------------------------
def Hinh15(n):
    print("Hình 15:")
    for dong in range (1,2*n):
        for cot in range (1,n+1):
            if dong>=cot and cot+dong<=2*n:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()
#-----------------------------------
def Hinh16(n):
    print("Hình 16:")
    for dong in range (1,2*n):
        for cot in range (1,n+1):
            if dong+cot>=n+1 and dong-cot<=n-1:
                print("* ", end=" ")
            else:
                print("  ", end=" ")
        print()

Hinh09(5)
Hinh10(5)
Hinh11(5)
Hinh12(5)
Hinh13(5)
Hinh14(5)
Hinh15(5)
Hinh16(5)