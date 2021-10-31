lst= list(map(int,input("Nhập nhiều số cách nhau bởi dấu phẩy").split(",")))
print("List vừa nhập: ",lst)

tong=0
for item in lst:
    tong=tong+item
print ("Cách 1: tổng các số có trong list=",tong)
print ("Cách 2: tổng các số có trong list=",sum(lst))

nho=lst[0]
for item in lst:
    if nho>item:
        nho=item
print ("Cách 1: số nhỏ nhất có trong list=",nho)
print ("Cách 2: số nhỏ nhất có trong list=",min(lst))


