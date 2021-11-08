# c18trg22
import math
#-----------------------------------
def KtraSNT(n):
    if (n<=1):
        return False
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i == 0):
            return False
    return True
#-----------------------------------
def CauA():
    PalindLst = lambda: InPalind()
    PalindLst()
#-----------------------------------
def InPalind():
    lst = []
    for i in range (2,1000001):
        i = str(i)
        if (i == i[::-1]):
            lst.append(i)
    print(lst)
#-----------------------------------
def CauB():
    PalindNTLst = lambda: InPalindNto()
    PalindNTLst()
#-----------------------------------
def InPalindNto():
    lst = []
    for i in range (2,1000001):
        if (KtraSNT(i) and str(i) == str(i)[::-1]):
            lst.append(i)
    print(lst)
#------------Chinh--------------
CauA()
CauB()