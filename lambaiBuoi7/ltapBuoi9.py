import csv
# ------------------------------------------------------------
def DocNoiDungFile_CSV_2(filename):
    try:
        with open(filename,'rt', encoding='utf8')as f:
            csvReaderObj = csv.reader(f)
            lst = csvReaderObj.__next__()
            print('-' * 76)
            print('|',lst[0].center(20),'|',lst[1].center(20),'|',lst[2].center(10),'|',lst[3].center(13),'|')
            print('-' * 76)
            for row in csvReaderObj:
                # print(row)
                print('|{:<21s}'.format(row[0]),'|','{:<20s}'.format(row[1]),'| %10s | %13s |'%(row[2],row[3]))
            # print(', '.join(field for field in fieldList))
    except FileNotFoundError:
        print('Tim ko thay tap tin')
# ------------------------------------------------------------
DocNoiDungFile_CSV_2('C:/Users/Abc/Documents/Thien_PythonFundamental_TTTH/buoi9_/DepartmentsV2.csv')