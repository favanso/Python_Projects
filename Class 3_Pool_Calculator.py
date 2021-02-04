"""
Fernando Branco
CIS 129
Pool Volume Calculator
"""
# Declare Variables
length = 0.0
width = 0.0
height = 0.0
volume_gallons = 0.0
gallons_converter = 7.5

#Get input

length = 5.0
width = 10.0
height = 12.0

#Complete calculations

volume_pool = length * width * height
volume_gallons = volume_pool*gallons_converter

#Output both volume and volume in gallons

print ('The volume of the pool is ', int(volume_pool))
print ('The volume in gallons is ',int(volume_gallons))
