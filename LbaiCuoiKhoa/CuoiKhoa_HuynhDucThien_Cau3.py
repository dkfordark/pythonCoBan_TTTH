# ----------------------------------------------------------
Cau3a = lambda a, b: print("Nghiem cua ptrinh la: ",-b/a) if (a != 0) else print('Ptrinh co so so nghiem') if (a==0 and b==0) else print('Ptrinh vo nghiem')
# ----------------------------------------------------------
Cau3b = lambda a,b,c,d,e,f: print('Nghiem cua ptrinh la x:%d\ty:%d:'%((c*e-b*f)/(a*e-b*d),(a*f-d*c)/(a*e-b*d))) if (a*e-b*d) !=0 else print('He ptrinh co vo so nghiem') if (a*e-b*d)==(c*e-b*f)==(a*f-d*c)==0 else print('He ptrinh vo nghiem')

# -------- Chuong trinh chinh -------------------------------
# ----- Cau 3 ----------------
print('--------Cau 3a-----------------------------')
# cau 3a
a,b = 2,6
Cau3a(a,b)
print('--------Cau 3b-----------------------------')
# cau 3b
a,b,c,d,e,f = 2, 1, 3, 1, -1, 6
# a,b,c,d,e,f = 1, -2, 1, 1, -2, 1 -> vo so nghiem
# a,b,c,d,e,f = 1, -2, 1, 3, -6, -3 -> vo nghiem
Cau3b(a,b,c,d,e,f)


