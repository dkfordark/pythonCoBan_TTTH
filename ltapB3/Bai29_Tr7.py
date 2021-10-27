print("Bai29/trg7")
n = int(input("vui long nhap n: "))
a = int(input("vui long nhap so hang dau tien: "))
p = int(input("vui long nhap cong boi: "))
if(n>0):
    i=0
    print("Cac so hang: ")
    while(i<n):
        i+=1
        a*=p
        print(a,end=" ")