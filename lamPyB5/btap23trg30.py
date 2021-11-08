def TachChuoi(lst,c):
    lst = s.split(c)
    print("list sau khi tach:", lst)
    return lst
# ------------------------------------------
def DemChuoi(lst):
    dem = 0
    for i in lst:
        if i != '':
            dem += 1
    print("Cach1: Dem ko xoa chuoi rong:%d" % dem)
# ------------------------------------------
def DemChuoiKoRong(lst):
    for i in range(len(lst) - 1, -1, -1):
        try:
            kt = lst[i]
            if kt == '':
                lst.remove(lst[i])
        except IndexError:
            print('IndexError: index = %d, khi len(lst)=%d' % (i, len(lst)))
    print('list sau khi xoa chuoi rong:', lst)
    print('Cach2: Dem sau khi da xoa chuoi rong:',len(lst))
# --------------Chuong trinh chinh----------
s = 'https://www.w3resource.com/python-excercises/string'
c = '/'
lst = TachChuoi(s,c)
print("So luong chuoi goc:",len(lst))
DemChuoi(lst)
DemChuoiKoRong(lst)




