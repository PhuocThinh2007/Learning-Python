name=input("Nhập họ tên:")

name=name.strip()
name=name.title()
while name.find("  ")!=-1:
    name=name.replace("  "," ")

print(name)

print("-"*40)

s=input("Nhập xâu:")
for i in range(10):
    s=s.replace(str(i),"")
print(s)
