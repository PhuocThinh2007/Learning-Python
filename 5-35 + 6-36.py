n=int(input("Nhập số nguyên dương n:"))
soUoc=0
while n<=0:
    print("n phải là số nguyên dương!")
    n=int(input("Nhập lại số nguyên dương n:"))
print("Các ước của {}:".format(n))
for i in range(n):
    if n%(i+1)==0:
        print(i+1,end=" ")
        soUoc+=1
print()
print()
print("Số ước của {}:".format(n),soUoc)