# c3trg26
# a
lst = list(map(int,input("nhap nhieu so cach nhau boi dau phay: ").split(",")))
print("List duoc nhap: ",lst)

# b
# lstC = []
# print("Cac so <5:",end='')
# for i in lst:
#     if i < 5:
#         print(i," ",end='')
#         lstC.append(i)
# # c
# print("\n")
# print("List cac so <5:",lstC)
#
# # d
# bsm = int(input("vui long nhap so m: "))
# print("cac boi so cua m: ",end='')
# for i in lst:
#     if i % bsm == 0:
#         print(i," ",end='')

# e
soluong = len(lst)
ze = am = duong = 0
for i in lst:
    if i > 0:
        duong +=1
        # print("ti le % cua so duong:",(duong/soluong*100))
    elif i < 0:
        am +=1
        # print("ti le % cua so duong:",(am/soluong*100))
    else:
        ze += 1
        # print(soluong - (am + duong) / (soluong*100))
print('%% số dương:{:0.2f}'.format(duong/(soluong) * 100))
print('%% số âm:{:0.2f}'.format(am/(soluong) * 100))
print('%% số 0:{:0.2f}'.format(ze/(soluong) * 100))
