def NhapSo():
    so=int(input("Nhập cạnh tam giác vuông: "))
    return so
#-------------------
def VeHinh01(n):
    print("Hình 01:")
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong+cot<=n+1):
                print("X ", end="")
            else:
                print("  ", end="")
        print()
#-------------------
def VeHinh02(n):
    print("Hình 02:")
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if (dong+cot>=n+1):
                print("X ", end="")
            else:
                print("  ", end="")
        print()
#-------------------
def VeHinh03(n):
    print("Hình 03:")
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==1 or cot==1 or dong+cot==n+1 :
                print("X ", end="")
            else:
                print("  ", end="")
        print()
#-------------------
def VeHinh04(n):
    for dong in range (1,n+1):
        for cot in range (1,n+1):
            if dong==n or cot==n or dong+cot==n+1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()
#-------------------
def VeHinh05(n):
    print('Hình 5')
    for dong in range(1, n+1):
        for cot in range(1, n+1):
            if cot - dong <= 0:
                print('* ', end = '')
            else:
                print('  ', end ='')
        print()
#-------------------
def VeHinh06(n):
    print('Hình 6')
    for dong in range(1, n+1):
        for cot in range(1, n+1):
            if cot - dong >= 0:
                print('* ', end = '')
            else:
                print('  ', end ='')
        print()
#-------------------
def VeHinh07(n):
    print('Hình 7')
    for dong in range(1, n+1):
        for cot in range(1, n+1):
            if dong == n or cot == 1 or dong == cot:
                print('*  ', end = '')
            else:
                print('   ', end ='')
        print()
#-------------------
def VeHinh08(n):
    print('Hình 8')
    for dong in range(1, n+1):
        for cot in range(1, n+1):
            if dong == 1 or cot == 5 or dong == cot:
                print('*  ', end = '')
            else:
                print('   ', end ='')
        print()
#-------------------
def menu():
    n=0
    while True:
        print("\nCHƯƠNG TRÌNH IN TAM GIÁC VUÔNG CÂN")
        print('\t0.- Nhập cạnh góc vuông của tam giác')
        print('\t1.- Vẽ hình 1')
        print('\t2.- Vẽ hình 2')
        print('\t3.- Vẽ hình 3')
        print('\t4.- Vẽ hình 4')
        print('\t5.- Vẽ hình 5')
        print('\t6.- Vẽ hình 6')
        print('\t7.- Vẽ hình 7')
        print('\t8.- Vẽ hình 8')
        print('\t9.- Kết thúc chương trình')
        print('\tBạn chọn chức năng (0-9):')
        chon=int (input("\tBạn chọn chức năng số: "))
        if chon==0:
            n=NhapSo()
        elif chon==1:
            VeHinh01(n)
        elif chon==2:
            VeHinh02(n)
        elif chon == 3:
            VeHinh03(n)
        elif chon==4:
            VeHinh04(n)
        elif chon==5:
            VeHinh05(n)
        elif chon==6:
            VeHinh06(n)
        elif chon==7:
            VeHinh07(n)
        elif chon==8:
            VeHinh08(n)
        elif chon == 9:
            print ("Bye Bye")
            break
        else:
            print("Chương trình chỉ nhận các số từ 0-9. Yêu cầu nhập lại.")