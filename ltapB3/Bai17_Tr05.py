print("Bai 17")
diem = int(input("Nhập điểm: "))
if diem < 0 or diem > 100:
    print("Chỉ nhận các giá trị từ 0 đến 100")
elif diem >= 90:
    print("Xếp loại A")
elif diem >= 80:
    print("Xếp loại B")
elif diem >= 70:
    print("Xếp loại C")
elif diem >= 65:
    print("Xếp loại D")
else:
    print("Xếp loại E")
