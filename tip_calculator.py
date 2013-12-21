base_cost = 20.00
tax_rate = 0.15
tip_rate = 0.15

print 'The base cost of your meal was $%.2f' % base_cost
tax_cost = tax_rate * base_cost
print 'You need to pay $%.2f for tax' % tax_cost
base_plus_tax = base_cost + tax_cost
tip_cost = tip_rate * base_plus_tax
print 'Tipping at a rate of %d%%, you should leave $%.2f for a tip' \
	% (int(100*tax_rate), tip_cost)
print 'The grand total of your meal is $%.2f' \
	% (base_cost + tax_cost + tip_cost)