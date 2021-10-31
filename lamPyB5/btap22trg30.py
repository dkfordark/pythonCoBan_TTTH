lst = ['ant','bear','cat','dog','elephant','fish','goat','hippo']
print("So thu trong list: ",len(lst))
print(lst)
s = input("moi nhap thu muon tim: ")
print(lst.count(s))
if lst.count(s) == 0:
    print("ko co thu muon tim")
else:
    print("co thu muon tim")
