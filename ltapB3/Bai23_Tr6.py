print("Cau23/p6")
print("Nhap toa do 3 dinh cua 1 tam giac")
xA, yA = map(eval,input("Nhap toa do x y cua diem A").split(" "))
xB, yB = map(eval,input("Nhap toa do x y cua diem B").split(" "))
xC, yC = map(eval,input("Nhap toa do x y cua diem C").split(" "))
print("Nhap toa do diem P")
xP, yP = map(eval,input("Nhap toa do x y cua diem P").split(" "))
z1 = (xB-xA) * (yP-yA) - (yB-yA) * (xP-xA)
z2 = (xC-xB) * (yP-yB) - (yC-yB) * (xP-xB)
z3 = (xA-xC) * (yP-yC) - (yA-yC) * (xP-xC)
if((z1>0 and z2>0 and z3>0) or (z1<0 and z2<0 and z3<0)):
    print("Diem P nam trong tam giac")
else:
    print("Diem P nam ngoai tam giac")