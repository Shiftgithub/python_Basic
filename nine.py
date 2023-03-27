myStr = input("Enter your string: ")
p = set(myStr)

s = {'0', '1'}

if s == p or p == {'0'} or p == {'1'}:
    print("Yes")
else :
    print("No")