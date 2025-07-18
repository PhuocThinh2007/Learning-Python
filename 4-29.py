n=int(input("Nhập số nguyên dương n:"))
while n<=0: n=int(input("Nhập lại số nguyên dương n:"))
print("-"*60)
k=0
while n>0:
    k+=n%10
    n=n//10
print("Tổng các chữ số của số N:",k)
