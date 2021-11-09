def conv(s,r,i):
    if i>len(s)-1:
        return r
    else:
        r=(r*10)+(ord(s[i])-48)
        return conv(s,r,i+1)
l='1234'
print(conv(l,0,0))