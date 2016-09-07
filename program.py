class Product:
	def__init__(self, price, count,tax):
		self.price = price
		self.count= count
		self.tax = tax

robot = Prouct(price=900, count=2, tax=1.25)
book = Prodcut(price=100,count=1, tax=1.06)



print(robot.price_with_tax() + book.price_with_tax())
