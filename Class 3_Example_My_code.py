"""
Fernando Branco
CIS 129
Pool Volume Calculator
"""
# Calculate volume of a poll
# Get input from console

length = input ('Input your poll`s length: ')
width = input ('Input your poll`s width: ')
height = input ('Input your poll`s height: ')

#Complete calculations

gallons_converter = 7.5
vol_pool = float (length) * float(width) * float(height)
vol_gallons = vol_pool*gallons_converter

#Output both volume and volume in gallons

print ('Your poll has ', vol_pool,' volume')
print ('Your poll has ',vol_gallons,' gallons')
