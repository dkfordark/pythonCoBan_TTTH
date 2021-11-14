def NhapSet(stt):
    myset = set()
    while True:
        x = int(input("Nhap so de them vao set "+str(stt)+"(Nhap -1 de ket thuc): "))
        if x == -1:
            return myset
        else:
            myset.add(x)
# ------------- chuong trinh chinh ----------------
set01 = NhapSet(1)
print(set01)
set02 = NhapSet(2)
print(set02)
# cau c
print("So luong ptu cua set: 1",len(set01))
print("Tong gia tri ptu cua set: 1",sum(set01))
print("So luong ptu cua set: 2",len(set02))
print("Tong gia tri ptu cua set: 2",sum(set02))
# cau d
print("Gia tri lon nhat cua set: 1",max(set01))
print("Gia tri lon nhat cua set: 2",max(set02))
print("Gia tri nho nhat cua set: 1",min(set01))
print("Gia tri nho nhat cua set: 2",min(set02))
# cau e
print("Ptu co trong set 1 hoac 2: ",set01 | set02)
# cau f
print("Ptu co trong set 1 va 2: ",set01 & set02)
# cau g
print("Ptu co trong set 1 va ko co o set 2: ",set01 - set02)
# cau h
print("Ptu co trong set 1 hoac 2 nhung ko phai chung: ",set01 ^ set02)
# cau i
print("Set 1 tang dan: ",sorted(set01))
print("Set 2 giam dan: ",sorted(set02,reverse=True))
