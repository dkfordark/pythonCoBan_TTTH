print('Câu 28')
n, a, d = map(int,input('Nhập n, a, d').split())
dem=1
while dem <= n:
    print(a,end=' ')
    a = a + d
    dem=dem+1
