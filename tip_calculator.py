import sys

if(len(sys.argv) != 4):
	print 'Usage: python tip_calculator.py meal tax tip'
	quit()

meal = float(sys.argv[1])
tax = float(sys.argv[2])
tip = float(sys.argv[3])

tax_value = 0.01 * tax * meal
meal_with_tax = meal + tax_value
tip_value = 0.01 * tip * meal_with_tax
total = meal_with_tax + tip_value

print 'The base cost of your meal was $%.2f' % meal
print 'You need to pay $%.2f for tax' % tax_value
print 'Tipping at a rate of %.2f%%, you should leave $%.2f for a tip' \
	% (tax, tip_value)
print 'The grand total of your meal is $%.2f' \
	% (total)