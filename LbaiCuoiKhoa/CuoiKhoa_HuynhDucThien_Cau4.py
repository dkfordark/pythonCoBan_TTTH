import csv
# --------------------------------------------------------------------------------
def InNoiDungFile_CSV(filename):
    SumCaseCum = 0
    SumCase24hrs = 0
    try:
        with open(filename,'rt',encoding='utf8')as f:
            csvReaderObj = csv.reader(f)
            lst = csvReaderObj.__next__()
            print('-' * 99)
            print('|',lst[0].center(20),'|',lst[2].center(30),'|',lst[6].center(40),'|')
            print('-' * 99)
            for row in csvReaderObj:
                if row[1]=='Western Pacific' and int(row[2])>50000 and (int(row[6])>100 and int(row[6])<2500):
                    print('|{:<21s}|{:>32s}|{:>42s}|'.format(row[0],row[2],row[6]))
                    SumCaseCum += int(row[2])
                    SumCase24hrs += int(row[6])
            print('-' * 99)
            print('|{:<21s}|{:>32d}|{:>42d}|'.format('SUM', SumCaseCum, SumCase24hrs))
            print('-' * 99)

    except FileNotFoundError:
        print('Tim khong thay tap tin')
# --------------------------------------------------------------------------------
def DocFile_CSV(filename):
    lstQuocGia = []
    lstLanhTho = []
    try:
        with open(filename,'rt',encoding='utf8')as f:
            csvReaderObj = csv.reader(f)
            lst = csvReaderObj.__next__()
            print('-' * 75)
            print('|',lst[0].center(39),'|',lst[1].center(30),'|')
            print('-' * 75)
            for row in csvReaderObj:
                if (row[1]=='Africa' or row[1]=='Europe' or row[1]=='South-East Asia') and int(row[2])==0:
                    print('|{:<40s}|{:>32s}|'.format(row[0],row[1]))
                    lstQuocGia.append(row[0])
                    lstLanhTho.append(row[0])
            print('-' * 75)
        return list(zip(lstQuocGia, lstLanhTho))
    except FileNotFoundError:
        print('Tim khong thay tap tin')
# --------------------------------------------------------------------------------
# Cau a
InNoiDungFile_CSV('E:/personal/Thien_PythonFundamental_TTTH/pythonCoBan_TTTH/de thi cuoi khoa/WHO-COVID-19-global-table-data.csv')
# cau b
lst =  DocFile_CSV('E:/personal/Thien_PythonFundamental_TTTH/pythonCoBan_TTTH/de thi cuoi khoa/WHO-COVID-19-global-table-data.csv')
print("List(Quoc gia, Lanh Tho):", lst)

