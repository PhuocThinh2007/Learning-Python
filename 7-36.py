n=int(input("Nhập số nguyên dương n:"))
soUoc=0
while n<=0:
    print("n phải là số nguyên dương!")
    n=int(input("Nhập số nguyên dương n:"))
for i in range(n):
    if n%(i+1)==0:
        soUoc+=1
if soUoc==2:
    print("{} là số nguyên tố".format(n))
else:
    print("{} không là số nguyên tố".format(n))