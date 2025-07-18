n=int(input("Nhập chiều dài cạnh tam giác:"))
while n<=0:
    print("chiều dài phải là số nguyên dương!")
    n=int(input("Nhập lại chiều dài cạnh tam giác:"))
for i in range(n):
    print("* "*(i+1))