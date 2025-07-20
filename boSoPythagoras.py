# Bộ số Pi-ta-go #
a, b, c = map(int,input("a, b, c: ").split())

a2 = a**2
b2 = b**2
c2 = c**2
if a2 == b2 + c2 or b2 == a2 + c2 or c2 == a2 + b2:
    print("Ba số đã nhập là bộ số Pi-ta-go")
else:
    print("Ba số đã nhập không là bộ số Pi-ta-go")