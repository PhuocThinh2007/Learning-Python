print("Đề 2:")
n=int(input("Nhập số nguyên dương n:"))
while n<=0:
    print("n phải là số nguyên dương!")
    n=int(input("Nhập số nguyên dương n:"))
print("-"*20)
print("Các số chẵn từ 1 tới {0}:".format(n))
for i in range(2,n+1,2):
    print(i,end=" ")
print()
print("-"*20)
tich=1
for i in range(1,n+1,2):
    tich=tich*i
print("Tích các số lẻ từ 1 tới {0} là: {1}".format(n,tich))
print("-"*60)
print("Đề 1:")
print("Câu 1:")
m=int(input("Nhập số nguyên dương m:"))
while n<=0:
    print("m phải là số nguyên dương!")
    m=int(input("Nhập số nguyên dương m:"))
print("-"*20)
print("Các số chẵn từ 1 tới {0}:".format(m))
for i in range(2,m+1,2):
    print(i,end=" ")
print()
print("Các số lẻ từ 1 tới {0}:".format(m))
for i in range(1,m+1,2):
    print(i,end=" ")
print()
print("-"*20)
tong=0
for i in range(n+1):
    tong+=i
print("Tổng các số từ 1 tới {0}: {1}".format(m,tong))
print("-"*20)
print("Bình phương các số chẵn là:")
for i in range(2,m+1,2):
    print(i**2,end=" ")
print()
print("-"*20)
print("Các ước số của m:")
for i in range(1,m+1):
    if m%i==0: print(i,end=" ")
print()
print("Câu 2:")
try:
    a=int(input("Nhập chiều dài a:"))
    b=int(input("Nhập chiều dài b:"))
    c=int(input("Nhập chiều dài c:"))
    if a>0 and b>0 and c>0 and a+b>c and b+c>a and c+a>b:
        print("Chiều dài 3 cạnh của tam giác là: {0},{1},{2}".format(a,b,c))
    else:
        print("Không có tam giác có chiều dài 3 cạnh như đã nhập.")
except:
    print("a,b,c phải là số nguyên dương")