# reading the amount of money deposited
amt = float(input('Enter the initial amount deposited to savings account:'))
# compute and display the amount in the account
ir = 4/100
# after 1 year
amt1 = amt+(amt*ir)
# after 2 years
amt2 = amt1+(amt1*ir)
# after 3 years
amt3 = amt2+(amt2*ir)
# Diaplay each amount so that it is rounded to 2 decimal places
print('total amount at the end of 1st year:', round(amt1, 2))
print('total amount at the end of 2nd year:', round(amt2, 2))
print('total amount at the end of 1nd year:', round(amt3, 2))
