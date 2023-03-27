mystr = input("Enter your string: ")

stringLen = len(mystr)
if stringLen > 7 and stringLen%2 != 0:
    first = mystr[0]
    middle = mystr[int(stringLen/2)]
    last = mystr[-1]
    newStr = first+middle+last
    print(newStr)
else:
    print("sorry you must entered greater than 7 character and odd number of character")