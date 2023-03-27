myStr = input("Enter your string: ")
myStrLen = len(myStr)
if myStrLen >= 3:
    if myStr[-3:] == 'ing':
        myStr = myStr+"ly"
        print(myStr)
    else:
        myStr = myStr + "ing"
        print(myStr)
else:
    print(myStr)