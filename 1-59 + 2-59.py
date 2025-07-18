n=int(input("Nhập số n nguyên dương:"))
a=[]
tong=0
while n<=0:
    print("n phải là số nguyên dương!")
    n=int(input("Nhập lại số n:"))
for i in range(n):
    a.append(input("Nhập số hạng thứ {}:".format(str(i+1))))
    tong+=int(a[i])
print(a)
print("Tổng là:",tong)
print("-"*40)
print("Các số chẵn trong dãy số là:")
for i in range(len(a)):
    if int(a[i])%2==0:
        print(a[i],end=" ")
print()