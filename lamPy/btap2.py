'''print('bai 4: cau A')
a = int(input('nhap so thu 1:'))
b = int(input('nhap so thu 2:'))
#print(a,'+',b,'=',a+b)
print("%d + %d = %d" %(a,b,a+b)) # decimal
print("{} + {} = {}".format(a,b,a+b))'''

'''print ("cauB")
a,b = input("nhap 2 so nguyen").split(",")
a = int(a)
b = int(b)
print("Ket qua: {} + {} = {}".format(a,b,a+b))'''

'''print ("cauC")
a,b = map(int,input("nhap 2 so nguyen").split(","))
print("Ket qua: {} + {} = {}".format(a,b,a+b))'''

'''print("cau5")
a,b = map(int,input("nhap 2 so nguyen").split())
print ("ket qua: %d^%d=%d"%(a,b,a**b))'''

'''print("cau6")
a = input("nhap 1 so nguyen: ")
a2 = a+a
a3 = a+a+a
t = int(a)+int(a2)+int(a3)
print ("ket qua a+aa+aaa: %s+%s+%s=%d"%(a,a2,a3,t))'''

'''print("cau8")
a,b,c = map(int,input("nhap 3 so nguyen cach nhau boi dau phay").split(","))
min(a,b,c)
print("Ket qua: {} + {} = {}".format(a,b,a+b))'''

'''print('cau')
a,b,c = map(float,input("nhap kich thuoc dai rong cao cach nhau boi dau phay").split(","))
print ("dien tich day: %.2f cm\u00b2 "%(a*b))
print ("The tich hcn: %.2f cm\u00b3"%(a*b*c))'''

'''a = int(input("nhap so thang:"))
print ("so tho: %d"%(2**(a+1)))'''

'''print("bai11")
r = eval(input("nhap ban kinh dtron > 0:"))
ht = r*r*3.14
hv = r*r
print("dien tich hinh vuong noi tiep: {}".format(ht-hv))'''

a = int(input("nhap so tien muon doi: "))
t500 = a // 500
t500du = a % 500
t200 = t500du // 200
t200du = t500du % 200
t100 = t200du // 100
t100du = t200du % 100
t50 = t100du // 50
t50du = t100du % 50
t20 = t50du // 20
t20du = t50du % 20
t10 = t20du // 10
t10du = t20du % 10
t5 = t10du // 5
t5du = t10du % 5
t2 = t5du // 2
t2du = t5du % 2
t1 = t2du // 1

print("Soto 500:{} 200:{} 100:{} 50:{} 20:{} 10:{} 5:{} 2:{} 1:{}".format(t500,t200,t100,t50,t20,t10,t5,t2,t1))
print("Loai 500 gom {}".format(t500))
print("Loai 200 gom {}".format(t200))
print("Loai 100 gom {}".format(t100))
print("Loai 50 gom {}".format(t50))
print("Loai 20 gom {}".format(t20))
print("Loai 10 gom {}".format(t10))
print("Loai 5 gom {}".format(t5))
print("Loai 1 gom {}".format(t1))

# if (t500 != 0):
#     print("Loai 500 gom {}".format(t500))
# if (t200 != 0):
#     print("Loai 200 gom {}".format(t200))
# if (t100 != 0):
#     print("Loai 100 gom {}".format(t100))
# if (t50 != 0):
#     print("Loai 50 gom {}".format(t50))
# if (t20 != 0):
#     print("Loai 20 gom {}".format(t20))
# if (t10 != 0):
#     print("Loai 10 gom {}".format(t10))
# if (t5 != 0):
#     print("Loai 5 gom {}".format(t5))
# if (t1 != 0):
#     print("Loai 1 gom {}".format(t1))


