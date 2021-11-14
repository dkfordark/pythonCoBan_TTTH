def uscln(a, b):
    if (b == 0):
        return a;
    return uscln(b, a % b);

print('USCLN: ',uscln(36,0))