lstCAN = ["Canh","Tan","Nham","Quy","Giap","At","Binh","Dinh","Mau","Ky"]
lstCHI = ["Than","Dau","Tuat","Hoi","Ty","Suu","Dan","Mao","Thin","Ty","Ngo","Mui"]

nam = int(input("nhap nam sinh duong lich: "))
print("Nam %d la nam %s %s"%(nam,lstCAN[nam%10],lstCHI[nam%12]))

