print("Cau24/p6")
x1, y1, r1 = map(int,input("vui long nhap x, y va r cho vong tron C1: ").split(","))
x2, y2, r2 = map(int,input("vui long nhap x, y va r cho vong tron C2: ").split(","))
c1c2 = ((x2-x1)**2 + (y2-y1)**2)**0.5
if(c1c2 <= r2):
    print("C1 nam trong C2")
elif(c1c2 <= r1):
    print("C2 nam trong C1")
elif(c1c2>abs(r2-r1) and c1c2<(r2+r1)):
    print("C1, C2 cat nhau")
elif(c1c2 > r1+r2):
    print("C1, C2 khong cat nhau")