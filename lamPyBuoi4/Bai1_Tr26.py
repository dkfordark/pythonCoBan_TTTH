lst=[1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]
print("List ban đầu:", lst)
for item in lst:
    if type(item)==int:
        print("kiểu dữ liệu của ", item, "là int")
    elif type(item)==float:
        print("kiểu dữ liệu của ", item, "là float")
    elif type(item)==complex:
        print("kiểu dữ liệu của ", item, "là complex")
    elif type(item)==bool:
        print("kiểu dữ liệu của ", item, "là boolean")
    elif type(item)==list:
        print("kiểu dữ liệu của ", item, "là list")
    elif type(item)==tuple:
        print("kiểu dữ liệu của ", item, "là tuple")
    elif type(item)==dict:
        print("kiểu dữ liệu của ", item, "là dictionary")
    elif type(item)==str:
        print("kiểu dữ liệu của ", item, "là string")
    else:
        print("Unknown")

print("tổng", sum(lst))