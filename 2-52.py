x=input("Nhập ngày tháng năm theo dạng dd/mm/yyyy: ")
while int(x[6:])<0:
    print("Năm nhập vào không hợp lệ")
    x = input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
while int(x[3:5])<0 or int(x[3:5])>12:
    print("Tháng nhập vào không hợp lệ")
    x=input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
if int(x[3:5]) in (1,3,5,7,8,10,12):
    while int(x[:2])<0 or int(x[:2])>31:
        print("Ngày nhập vào không hợp lệ")
        x=input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
if int(x[3:5]) in (4,6,9,11):
    while int(x[:2])<0 or int(x[:2])>30:
        print("Ngày nhập vào không hợp lệ")
        x=input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
if x[3:5]==2:
    if (int(x[6:])%4==0 and int(x[6:])%100!=0) or int(x[6:])%400==0:
        while int(x[:2])<0 or int(x[:2])>29:
            print("Ngày nhập vào không hợp lệ")
            x=input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
    else:
        while int(x[:2])<0 or int(x[:2])>28:
            print("Ngày nhập vào không hợp lệ")
            x=input("Nhập lại ngày tháng năm theo dạng dd/mm/yyyy: ")
d=x[:2]
m=x[3:5]
y=x[6:]
print("Ngày {} tháng {} năm {}".format(d,m,y))