x=0
print("{0:>3}{1:>12}".format("STT","Giá trị"))
print("-"*60)

while(x<10):
    x=x+1
    print("{0:>3}{1:>12}".format(x,10**(11-x)))
