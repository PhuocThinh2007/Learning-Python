import math

r=float(input("Nhập bán kính:"))
while(r<=0):
    print("Bán kính phải là một số dương.Vui lòng thử lại.")
    r=float(input("Nhập lại bán kính:"))
print("Chu vi hình tròn:",2*r*math.pi)
print("Diện tích hình tròn:",math.pi*r*r)

