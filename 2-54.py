fileName=input("Nhập tên file:")
length=len(fileName)

extensionName=fileName[length-3:]
if extensionName==".py":
    print("True")
else:
    print("False")
