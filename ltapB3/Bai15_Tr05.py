print("Bai 15a")
n = int(input("Nhập 1 sô nguyên: "))    # 7//2=>3
if n % 2 == 0:                          # 7%2=>1 modulo
    print ("%d là số chẵn" %(n))
else:
    print("%d là số lẻ" % (n))

print("Bai 15b")
if n % 4 == 0:
    print('%d là số chia hết cho 4' % (n))
elif n % 2 == 0:
    print('%d là số chia hết cho 2' % (n))
else:
    print('%d không chia chẵn cho cả 4 và 2')

print('Câu c')
m = int(input('Nhập số chia: '))
if n % m ==0:
    print('%d chia hết cho %d'%(n,m))
else:
    print('%d không chia hết cho %d'%(n,m))
