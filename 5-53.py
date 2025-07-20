s=input("Nhập xâu bất kì:")
for i in range (10):
    s=s.replace(str(i),"", s.count(str(i)))
print("Xâu sau khi xóa các kí tự số:",s)
print()