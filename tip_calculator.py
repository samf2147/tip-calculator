meal = 20.00
tax = 0.15
tip = 0.15

tax_value = tax * meal
meal_with_tax = meal + tax_value
tip_value = tip * meal_with_tax
total = meal_with_tax + tip_value

print 'The base cost of your meal was $%.2f' % meal
print 'You need to pay $%.2f for tax' % tax_value
print 'Tipping at a rate of %d%%, you should leave $%.2f for a tip' \
	% (int(100*tax), tip_value)
print 'The grand total of your meal is $%.2f' \
	% (total)