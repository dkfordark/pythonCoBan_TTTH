def TinhPhanTram(lst):
    nd = na = n0 = 0
    for i in lst:
        if i > 0:
            nd += 1
        elif i < 0:
            na += 1
        else:
            n0 += 1
    return nd,na,n0
#---------------------------------------------
lst = [1, -1, 2, 0, 5, 8, -13, 21, -34, 55, 87, 0]
print("List ban đầu: ",lst)
print("Câu B:")
lstC = []
print("Cac so <5:",end='')
for i in lst:
    if i < 5:
        print(i," ",end='')

print("\nCâu C:")
for i in lst:
    if i < 5:
        lstC.append(i)
print("List cac so <5:",lstC)

print("\nCâu D:")
bsm = int(input("vui long nhap so m: "))
print("cac boi so cua m: ",end='')
for i in lst:
    if i % bsm == 0:
        print(i," ",end='')

print("\nCâu E:")
nd,na,n0=TinhPhanTram(lst)
print('Số dương chiếm tỷ lệ: {:.2f}%'.format((nd*100)/(nd+na+n0)))
print('Số âm chiếm tỷ lệ: {:.2f}%'.format((na*100)/(nd+na+n0)))
print('Số zero chiếm tỷ lệ: {:.2f}%'.format((n0*100)/(nd+na+n0)))