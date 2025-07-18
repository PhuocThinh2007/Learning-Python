from math import *
try:
    a=int(input("Nhập hệ số a:"))

    if a!=0:
        b = int(input("Nhập hệ số b:"))
        c = int(input("Nhập hệ số c:"))
        print("-" * 60)
        print("Giải phương trình {0}x^2+{1}x+{2}=0".format(a, b, c))
        delta=b**2-4*a*c
        if delta<0: print("Phương trình vô nghiệm")
        elif delta==0: print("Phương trình có nghiệm kép x1 = x2 =",-b/(2*a))
        else:
            x1=(-b-sqrt(delta))/(2*a)
            x2=(-b+sqrt(delta))/(2*a)
            print("Phương trình có 2 nghiệm phân biệt x1 = {0} và x2 = {1}".format(x1,x2))
    else: print("Hệ số a phải khác 0")
except:
    print("Hệ số phải là số nguyên")