import math

class Point(object):
	def __init__ (self, x = 0, y = 0):
		self.x = x
		self.y = y
		
def calculate_distance(p1, p2):
	distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
	return distance

p1 = Point(0,0)
p2 = Point(1,1)

print(calculate_distance(p1, p2))