print("Bai25")
a, b, c, d, e, f = map(eval, input("Vui long nhap 6 so thuc: ").split(";"))
D = a * e - b * d
Dx = c * e - b * f
Dy = a * f - d * c
print("D:{}\tDx:{}\tDy:{}".format(D, Dx, Dy))
if (D == 0):
    if (Dx == 0 and Dy == 0):
        print("Ptrinh co vo so nghiem")
    else:
        print("Ptrinh vo nghiem")
else:
    print("Ptrinh co 1 nghiem")
    x = Dx / D
    y = Dy / D
    print(("Gia tri x:{} y:{}").format(x, y))