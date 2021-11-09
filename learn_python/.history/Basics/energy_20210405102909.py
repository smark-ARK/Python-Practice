m = float(input("Enter the mass of water in ml: "))
chT = float(input('Enter the difference u want to make in Temperature (in C): '))
C = 4.186
q = m*C*chT
jtokwh = 2.77778e-7
print("The Amount of energy needed to make the change is: ", q, 'Joules')
