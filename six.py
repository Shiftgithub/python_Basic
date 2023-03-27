myStr = input("Enter your string: ")

myStrLen = len(myStr)
if myStrLen > 2:
    newStr = myStr[:2]+myStr[-2:]
    print(newStr)
else:
    print("")