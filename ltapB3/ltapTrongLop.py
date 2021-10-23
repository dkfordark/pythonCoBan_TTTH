a, b = map(int,input("vui long nhap 2 so nguyen: ").split())
print("tu a -> b")
if (a>b):
    a,b = b,a

for i in range(a,b+1):
    print("bang cuu chuong %d"%i)
    for j in range(1,11):
        print("%d x %d = %d"%(i,j,i*j))


n = a
while n<b+1:
    print("bang cuu chuong: %d"%n)
    i = 1
    while i<10:
        print ("%d x %d = %d"%(i,n,i*n))
        i+=1
    n+=1
