with open("TextFiles/learning_python.txt") as ob:
    # print(ob.read())
    lines = ob.readlines()
    # for line in ob:
    # print(line)
for i in lines:
    # print(i)
    print(i.replace("Python", "JavaScript"))
