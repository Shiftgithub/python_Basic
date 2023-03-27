mystr = input("Enter your string: ")

lenStr = len(mystr)
first = mystr[0]
middle = mystr[int(lenStr/2)]
last = mystr[-1]
newStr = first+middle+last
print(newStr)
