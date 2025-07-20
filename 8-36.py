n=int(input("Nhập số nguyên dương n:"))
soUoc=0
while n<=0:
    print("n phải là số nguyên dương!")
    n=int(input("Nhập số nguyên dương n:"))
print("Các số nguyên tố từ 1 tới n:")
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%j==0:
            soUoc+=1
    if soUoc==2:
        print(i,end=" ")
    soUoc=0
print()