Can=["Canh","Tân","Nhâm","Quý","Giáp","Ất","Bính","Đinh","Mậu","Kỷ"]
Chi=["Thân","Dậu","Tuất","Hợi","Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi"]

nam=int(input("Nhập năm dương lịch: "))
print("Năm %d là năm %s %s" %(nam, Can[nam%10], Chi[nam%12]))


