def maNhiPhan(t):
    NhiPhan=0
    while t!=0:
        for i in range(8):
            NhiPhan+=(t%2)*10**i
            t//=2
    return NhiPhan

n=int(input("Nhập n:"))
while n>255 or n<0:
    print("n không hợp lệ")
    n=int(input("Nhập lại n:"))
print("Mã nhị phân của",n,"là","{}{}".format("0"*(8-len(str(maNhiPhan(n)))),maNhiPhan(n)))