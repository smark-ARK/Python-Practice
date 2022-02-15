with open("Basics/File_Handling/TextFiles/digits.txt") as file_object:
    lines = file_object.readlines()
pi_string = ""
for i in lines:
    pi_string += i.strip()

print(f"Value of pi is: {pi_string} and length is: {len(pi_string)}")
print()
