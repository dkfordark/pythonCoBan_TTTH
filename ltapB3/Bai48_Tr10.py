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
def menu():
    n=0
    while True:
        print("\nCHƯƠNG TRÌNH IN TAM GIÁC VUÔNG CÂN")
        print('\t0.- Nhập cạnh góc vuông của tam giác')
        print('\t1.- Vẽ hình 1')
        print('\t2.- Vẽ hình 2')
        print('\t5.- Vẽ hình 5')
        print('\t6.- Vẽ hình 6')
        print('\t9.- Kết thúc chương trình')
        print('\tBạn chọn chức năng (0-9):')
        chon=int (input("\tBạn chọn chức năng số: "))
        if chon==0:
            n=NhapSo()
        elif chon==1:
            VeHinh01(n)
        elif chon==2:
            VeHinh02(n)
        elif chon==5:
            VeHinh05(n)
        elif chon==6:
            VeHinh06(n)
        elif chon == 9:
            print ("Bye Bye")
            break
        else:
            print("Chương trình chỉ nhận các số từ 0-9. Yêu cầu nhập lại.")
#-------------------    chương trình chính  --------------------
menu()