n = int(input("Nhap so tien: ")) # n =1234
tong_so_to = 0
to_500 = n// 500
n=n%500
if (to_500 != 0):
    print("Loai 500 gom {}".format(to_500))

to_200 = n//200
n=n%200
if (to_200 != 0):
    print("Loai 200 gom {}".format(to_200))

to_100 = n//100
n=n%100
if (to_100 != 0):
    print("Loai 100 gom {}".format(to_100))

to_50 = n//50
n=n%50
if (to_50 != 0):
    print("Loai 50 gom {}".format(to_50))

to_20 = n//20
n=n%20
if (to_20 != 0):
    print("Loai 20 gom {}".format(to_20))

to_10 = n//10
n=n%10
if (to_10 != 0):
    print("Loai 10 gom {}".format(to_10))
to_5 = n//5
n=n%5
if (to_5 != 0):
    print("Loai 5 gom {}".format(to_5))
to_2 = n//2
n=n%2
if (to_2 != 0):
    print("Loai 2 gom {}".format(to_2))
to_1 = n//1
n=n%21
if (to_1 != 0):
    print("Loai 1 gom {}".format(to_1))
print("tong so to tien",to_500+to_200+to_100+to_50+to_20+to_10+to_5+to_2+to_1)
