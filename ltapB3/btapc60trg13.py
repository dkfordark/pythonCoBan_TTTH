s = "HeLLO PyThoN HelloH"
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())

# b
# c = input("Vui long nhap ky tu: ")
# # cach1
# count = 0
# for i in range (0,len(s)):
#     if s[i] == c:
#         count += 1
# print(count)
# cach2
# print(s.count(c,0,len(s)))

# c
# numCount=0
# alpCount=0
# for i in range (0, len(s)):
#     if s[i].isnumeric():
#         numCount+=1
#     elif s[i].isalpha():
#         alpCount+=1
# print("co %d ky tu va %d ky so"%(alpCount,numCount))

# d
# ktHoa=0
# ktThuong=0
# ktSo=0
# ktConLai=0
# for i in range (0, len(s)):
#     if s[i].isupper():
#         ktHoa+=1
#     elif s[i].islower():
#         ktThuong+=1
#     elif s[i].isnumeric():
#         ktSo+=1
#     else:
#         ktConLai+=1
# print("co %d ky tu Hoa_\t%d ky tu thuong_\t%d ky tu so_\t%d ky tu con lai"%(ktHoa,ktThuong,ktSo,ktConLai))

# e
paCount = 0
naCount = 0
s = s.lower()
for i in range (0,len(s)):
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u':
        paCount+=1
    else:
        naCount+=1
print("Phu am: %d\tNguyen am: %d"%(paCount,naCount))