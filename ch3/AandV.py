# AandV.py

def arvol(radius):
	import math
	volume = float(4)/3 * math.pi * radius**3
	area = 4 * math.pi * radius**2
	return volume, area

print arvol(2.5)
