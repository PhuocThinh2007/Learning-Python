import math
def BCNN(a,b):
    return a*b/math.gcd(a,b)
a=int(input("Nhập số nguyên a:"))
b=int(input("Nhập số nguyên b:"))
print("BCNN của a và b:",BCNN(a,b))
