from math import *
n=int(input("Nhập số nguyên dương n:"))
while n<=0:
    print("n phải là số nguyên dương!")
    n = int(input("Nhập số nguyên dương n:"))
print("-"*60)
tong=tongLe=tongChan=0
print("Các số từ 1 tới {0} là:".format(n))
for i in range(1,n+1):
    print(i,end=" ")
    tong+=i
print()
print("Tổng các số từ 1 tới {0}: {1}".format(n,tong))
print("Tích các số từ 1 tới n:",perm(n))
print("-"*60)

print("Các số lẻ từ 1 tới n là:")
for j in range(1,n+1,2):
    print(j,end=" ")
    tongLe+=j
print()
print("Tổng các số lẻ từ 1 tới {0}: {1}".format(n,tongLe))
print("-"*60)

print("Các số chẵn từ 1 tới n là:")
for k in range(2,n+1,2):
    tongChan+=k
    print(k,end=" ")
print()
print("Tổng các số chẵn từ 1 tới {0}: {1}".format(n,tongChan))