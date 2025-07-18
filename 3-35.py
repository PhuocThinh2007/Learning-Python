tich=1
for i in range(1,11):
    for k in range(2,10):
        tich=k*i
        if i<10:
            if tich<10: print("{}* {} = {}".format(k,i,tich),end="  ")
            else: print("{}* {} ={}".format(k,i,tich),end="  ")
        else: print("{}*{} ={}".format(k,i,tich),end="  ")
    print()
print("-"*40)
tich=1
for i in range(1,11):
    for k in range(2,10):
        tich=k*i
        print("{}*{}={}".format(k,i,tich),end="\t")
    print()
print("-"*40)
#Mở rộng
n=int(input("Nhập bảng cửu chương cần tra:"))
while n<2 or n>9:
    print("Chỉ xuất đuọc bảng cửu chương từ 1 tới 9")
    n = int(input("Nhập lại bảng cửu chương cần tra:"))
for i in range(1,10):
    print("{} * {} = {}".format(n,i,n*i),end="\t")
    print()
print("{} *10 = {}".format(n,n*10))