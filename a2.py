# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.
units = int(input("please enter the amount of electricity units consumed"))
# 2) Use if–elif–else to decide the cost based on `units`:
if units < 50:
    amount = ((units*2.60)+25)
elif units <= 100 and units > 50:
    amount = ((50*2.60)+((units-50)*3.25)+35)
elif units <= 200 and units > 100:
    amount = ((50*2.60)+((units-50)*3.25)+((units-100)*5.26)+45)
else:
    amount = ((50*2.60)+((units-50)*3.25)+((units-100)*5.26)+((units-200)*8.45)+75)

total = amount
print(round(amount,2))

# 3) Calculate the final bill:
#    total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places.