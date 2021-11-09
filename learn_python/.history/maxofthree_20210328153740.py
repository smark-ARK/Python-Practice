def max(x, y, z):
    if (x > y & x > z):
        print("x is greater")
    elif(y > x & y > z):
        print("Y is the greatest")
    elif(z > x & z > y):
        print("Z is the greatest")


max(10, 50, 10)
