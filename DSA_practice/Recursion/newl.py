def sumnn(s):
    i=input("Number: ")
    if i==" ":
        return 0
    else:
        int(i)
        if type(i)==type(0):
            s+=i
            print(s)
            return sumnn(s)
        return s
s=0      
print(sumnn(s))