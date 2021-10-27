print("Bai 26")
a, b, c = map(int,input("Nhập ba số nguyên cách nhau bởi dấu phẩy: ").split(","))
d = b-a
g = b//a

if b+d == c:
    print("Là cấp số cộng với dãy {}, {}, {}, {},...".format(a,b,c,c+d))
elif b*g == c:
    print("Là cấp số nhan với dãy {}, {}, {}, {},...".format(a, b, c, c * g))
else:
    print("Không phải là cấp số cộng và cấp số nhân")



