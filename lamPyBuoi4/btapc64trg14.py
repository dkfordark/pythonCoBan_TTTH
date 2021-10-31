# c64trg14
s = '''     Quê hương
Quê hương là   chùm khế   ngọt.
    Cho con trèo hái   mỗi  ngày   .
Quê  hương là   đường  đi học .
  Con về  rợp bướm  vàng bay .
  Đỗ     Trung Quân    
'''

s = s.strip()
# print(s[2])

# s = "hello word"
# print(s[10])

# print(s.count(" "))

# count = 0
# for i in s:
#     if i == "\n":
#         count = 0
#     elif i == " ":
#         count += 1
#         if count = 2:
#             continue
#     print(i,end='')
#     count = 0

# count = 0
# for i in range (0,len(s)):
#     if s[i-1] == s[i] == " ":
#         continue
#     else:
#         print(s[i],end='')

s = s.split("\n")
# m = "abc"
# print(s[1])
# M[1] = s[1]

for i in range(0,len(s)):
    m = s[i]
    for j in range (0,len(m)):
        if m[j-1] == m[j] == " ":
            continue
        else:
            print(m[j],end='')
    print("\n")


# sM = s[1]
# for i in range (0,len(sM)):
#     if sM[i-1] == sM[i] == " ":
#         continue
#     else:
#         print(sM[i],end='')
