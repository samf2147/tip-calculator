from optparse import OptionParser

parser = OptionParser()

parser.add_option('-m','--meal',dest = 'meal', 
	help = 'the cost of the meal in dollars')
parser.add_option('-x','--tax',dest = 'tax',
	help = 'the tax rate')
parser.add_option('-t','--tip',dest = 'tip',
	help = 'the tip rate', default = '15.0')
	
(options,args) = parser.parse_args()

if not (options.meal and options.tax):
	parser.error('Need an argument for -m and -x')


meal = float(options.meal)
tax = float(options.tax)
tip = float(options.tip)

tax_value = 0.01 * tax * meal
meal_with_tax = meal + tax_value
tip_value = 0.01 * tip * meal_with_tax
total = meal_with_tax + tip_value

print 'The base cost of your meal was $%.2f' % meal
print 'You need to pay $%.2f for tax' % tax_value
print 'Tipping at a rate of %.2f%%, you should leave $%.2f for a tip' \
	% (tip, tip_value)
print 'The grand total of your meal is $%.2f' \
	% (total)