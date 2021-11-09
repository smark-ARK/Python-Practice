p = float(input('Enter the Amount of pressure in pascals:'))
v = float(input('Enter the volume of GAS:'))
r = 8.314
tC = float(input('Enter the teperature in celcius:'))
tK = tC + 273.15
n = (p*v)/(r*tK)


print('The no of moles in gas:', n)

pinS = 20, 000, 000
tCinS = 20
vinS = 12
