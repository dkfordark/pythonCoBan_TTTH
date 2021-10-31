# nhập số. In ra chử số tương ứng   9452, 21, 789654312
def InChuSo(n):
    ChuSo=['không','một','hai','ba','bốn','năm','sáu','bảy','tám','chín']
    if n<0:
        print('am ', end=' ')
        n=-1*n
    #Cách  1: đảo chuỗi
    '''so=int(str(n)[::-1])
    while so>0:
        kq=so%10
        print('%s' % ChuSo[kq], end=' ')
        so=so//10
    '''
    # Cách  2: không đảo
    k=1
    while k*10<n:
        k=k*10
    while k>0:
        kq=n//k
        print('%s' % ChuSo[kq], end=' ')
        n=n%k
        k=k//10
#-------------------------------------
InChuSo(-123456789)

