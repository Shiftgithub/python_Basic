mystr = input("Enter your string: ")


stringLen = len(mystr)
first = mystr[0]
middle = mystr[int(stringLen/2)]
last = mystr[-1]

newStr = first+middle+last
print(newStr)