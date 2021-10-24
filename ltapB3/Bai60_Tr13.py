def NhapChuoi():
    chuoi = input('Nhập chuỗi:')
    return chuoi
def NhapKyTu():
    chuoi = input('Nhập ký tự:')
    return chuoi
def ThucHienB_1(s, ch):
    dem = 0
    for i in range(0, len(s)):
        if ch == s[i]:
            dem += 1
    return dem

def ThucHienB_2(s,ch):
    dem = s.count(ch, 0, len(s))
    return dem
#====   chuong trinh chinh  ==================
s = NhapChuoi()
print ("Câu A: ")
print ("UPPER:",s.upper())
print ("lower:",s.lower())
print ("Title:",s.title())
print ("Title:",s.capitalize())
print ("swapcase:",s.swapcase())

print ("Câu B: ")
ch = NhapKyTu()
print('Trong s có %d ký tự %s (dùng For và if)'%(ThucHienB_1(s, ch), ch))
print('Trong s có %d ký tự %s (dùng count)'%(ThucHienB_2(s, ch), ch))

print ("Câu C: ")
numCount=0
alpCount=0
for i in range (0, len(s)):
    if s[i].isnumeric():
        numCount+=1
    elif s[i].isalpha():
        alpCount+=1
print("co %d ky tu va %d ky so"%(alpCount,numCount))

print ("Câu D: ")
ktHoa=0
ktThuong=0
ktSo=0
ktConLai=0
for i in range (0, len(s)):
    if s[i].isupper():
        ktHoa+=1
    elif s[i].islower():
        ktThuong+=1
    elif s[i].isnumeric():
        ktSo+=1
    else:
        ktConLai+=1

print("Co %d ky tu Hoa"%(ktHoa))
print("Co %d ky tu thuong"%(ktThuong))
print("co %d ky tu so"%(ktSo))
print("co %d ky tu con lai"%(ktConLai))

print ("Câu E: ")
vowel="AEIOU"
consonant="BCDFGHJKLMNPQRSTVWXYZ"
sNguyenAm=sPhuAm=""
for i in s:
    if i.upper() in vowel:
        if i not in sNguyenAm:
            sNguyenAm += i
    elif i.upper() in consonant:
        if i not in sPhuAm:
            sPhuAm += i
print("co %d nguyen am: %s"%(len(sNguyenAm),", ".join(sNguyenAm)))
print("co %d phu am: %s"%(len(sPhuAm),", ".join(sPhuAm)))
