print("bai 27A:")
# a
n = int(input("vui long nhap so n: "))
i = 0
while (i<n):
    i += 1
    print ('so:',i)
#-------------------------------------
print("Bài tập 27b")
n = int(input("Nhập số nguyên n: "))
print("Cách 1: Các bội số của 5 và nhỏ hơn %d" %n)
i = 5
while i < n :
    i +=5
    print("số:", i,end=" " )
print("\nCách 2: Các bội số của 5 và nhỏ hơn %d" %n)
i = 1
while i < n :
    if i%5==0:
        print("số:", i,end=" " )
    i += 1
#-------------------------------------
print("bai17c")
n = int(input("vui long nhap so n: "))
i = 0
s = 0
while (i<n):
    i += 1
    s += i
print ("Tổng các số từ 1 đến %d là %d" %(n,s))
#-----------------------------------------------
print("Bai 27d")
n = int(input("Nhập số nguyên n: "))
i = 2
tong = 0
while i<n:
    if i % 2 == 0:
        tong +=i
    i +=2
print("tong so chan:", tong)

print("bai17e")
n = int(input("vui long nhap so n: "))
i = 0
s = 0
print ("Cac uoc so chan cua %d la: ",n, end=" ")
while (i<=n):
    i += 1
    if (i%2==0):
        a = i // 2
        s += a
        print (a, end=" " )
print ("\nTong cac uoc so chan cua %d la %d: " %(n,s))

print("bai 27F")
n = int(input("vui long nhap so n: "))
print("Cach 1: di tu nho den lon:")
i = 0
kq=0
while (i<n):
    if (i%2==0):
        kq=i
        i+=2
print ("So chan nho hon va gan voi %d nhất là %d" %(n,kq))
print("Cach 2: di tu lon ve nho:")
if (n%2==0):
     kq=n-2
else:
    kq = n - 1
print ("So chan nho hon va gan voi %d nhất là %d" %(n,kq))

print('Câu 27 G: cách 1: đi từ lớn về nhỏ')
n = int(input('Nhập số nguyên n: '))
t=n-1
while t < n:
    if n%t == 0 and t%2 != 0:
        break
    t=t-1
print('Ước số lẻ lớn nhất của %d là: %d'%(n,t))

print("bai27g")
print("Cach 2: di tu nho den lon:")
n = int(input("vui long nhap so n: "))
i = 1
kq=1
while (i<n):
    if n%i==0 and i%2==1:
        kq=i
    i+=1
print ("Uoc so le lon lon nhat cua %d là %d" %(n,kq))











