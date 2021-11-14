chuoiNhap = input("Moi nhap chuoi: ")
chuoiNhap=set(chuoiNhap.lower())
print(chuoiNhap)

chuThuong = []
for i in range (97,123):
    chuThuong.append(chr(i))
set(chuThuong)

print("Cac chu ko co : ",end='')
for i in chuThuong:
    if i not in chuoiNhap:
        print(i,end=' ')
