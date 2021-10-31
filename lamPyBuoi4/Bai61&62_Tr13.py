#Bài tập về nhà: 61,62,63 trang 13;  49 trang 11
def Bai61(S):
    for index in range(len(S)):
        if index%2==0:
            print(S[index].upper(),end="")
        else:
            print(S[index].lower(),end="")
    print()
#----------------
def Bai62A(S):
    if len(S)>4:
        print(S[::-1])
    else:
        print(S)
#----------------
def Bai62B(S):
    upp=low=0
    #B1: dếm ký tự hoa/thường
    for index in range(len(S)):
        if S[index].isupper():
            upp+=1
        elif S[index].islower():
            low+=1
    #B2: xử lý
    if upp>=low:
        print(S.upper())
    else:
        print(S.lower())
    print()
#----------------



S="Sai goN quan 5"
S2="Sg5"
Bai61(S)
Bai62A(S)
Bai62B(S)
Bai62B(S2)
