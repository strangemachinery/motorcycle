class Wheels(object):
	def __init__(self, weight, cost, name):
		self.weight = weight
		self.cost = cost
		self.name = name
	
wheeltype1 = Wheels(9, 30, "chrome")
wheeltype2 = Wheels(10, 31, "billet")
wheeltype3 = Wheels(4, 50, "laced")

class Frames(object):
#	type = ["aluminum","carbon","steel"]
	def __init__(self, type, weight, cost):
		self.type = type
		self.weight = weight
		self.cost = cost

frame1 = Frames("aluminum", 4, 4)
frame2 = Frames("carbon", 5, 5)
frame3 = Frames("steel", 5, 10)
	
class Models(object):
	def __init__(self, wheel1, wheel2, frame, name):
		self.wheel1 = wheel1
		self.wheel2 = wheel2
		self.frame = frame
		self.name = name
	def cost(self):
		return self.wheel1.cost + self.wheel2.cost + self.frame.cost
	def weight(self):
		return self.wheel1.weight + self.wheel2.weight + self.frame.weight
	
class Manufacturer(object):
	inventory = []
	def __init__(self, name, percentage, inventory):
		self.name = name
		self.percentage = percentage
		self.inventory = inventory

man1 = Manufacturer("California", 0.04)
man2 = Manufacturer("Australia", 0.05)

class Shop(object):
	inventory = []
	def __init__(self, name, inv, price, profiting):
		self.name = name
		self.inv = inv
		self.price = price
		self.profiting = profiting 


class Customer(object):
	def __init__(self, name, budget):
		self.name = name
		self.budget = budget
		self.purchase = purchase
	def leftover(self):
		for num in self.budget:
			self.budget -= self.purchase()
		return "You have {} left over.".format(self.budget)
		if self.purchase >= budget:
			print "You have enough for this. You're fine"
		else:
			print "Sorry. You need to keep saving"


#wheels1 = Wheels.wheel_type1(9, 30, "chrome")

#man1 = Manufacturer("California", 0.04)
#man2 = Manufacturer("Australia", 0.05)
cust1 = Customer("Michael", 200)
cust2 = Customer("Jeff", 500)
cust3 = Customer("Steven", 1000)

