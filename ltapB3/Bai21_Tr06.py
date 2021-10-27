print("bai21" )
a, b = map(int,input("vui long nhap 2 so nguyen cach nhau boi dau ,: ").split(","))
if (a == 0 and b == 0):
    print("phuong trinh vo so nghiem")
elif (a == 0 and b != 0):
    print("phuong trinh co vo so nghiem")
else:
    x = -b / a
    print("ket qua: %d",x)
