def bdNgang():
    for dong in range(0,4):
        for cot in range(0,7):
            if (dong==0 and (cot==0 or cot==1)):
                print("*\t",end='')
            elif (dong==2):
                print("*\t",end='')
            elif (dong==3 and (cot==0 or cot==1 or cot==2)):
                print("*\t",end='')
            else:
                print(" \t",end='')
        print("\n")
# --------------------------------------------
def bddoc():
    for dong in range(0,7):
        for cot in range(0,4):
            if (cot==0 and dong>4):
                print("*\t",end='')
            else:
                print (" \t",end='')
            if (cot==1):
                print(" \t",end='')
            elif (cot==2):
                print("*\t",end='')
            elif (cot==3 and dong>3):
                print("*\t", end='')
        print("\n")
# --------------Chuong trinh chinh------------
# bdNgang()
# bddoc()


