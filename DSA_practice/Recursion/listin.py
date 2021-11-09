def listin(l,i,n):
    if i>n-1:
        return l
    else:
        l[i]=int(input('Enter element: '))
        i+=1
        return listin(l,i,n)

n=int(input("number: "))
l=[0]*n
print(l)
listin(l,0,n)
print(l)