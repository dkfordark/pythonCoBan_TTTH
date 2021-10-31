def Bai64(S):
    S=S.strip()
    while S.find("  ")>0:
        S=S.replace("  ", " ")
    while S.find("\n ")>0:
        S=S.replace("\n ", "\n")
    while S.find(" .")>0:
        S=S.replace(" .", ".")
    return S

#------  chương trình chính ---------------------
S='''     Quê hương
Quê hương là                                       chùm khế ngọt  .\n
     Cho con trèo hái    mỗi ngày.
Quê    hương là đường đi học   .
    Con về    rợp bướm   vàng bay.
 Đỗ     Trung Quân       '''
S=Bai64(S)
print(S)
