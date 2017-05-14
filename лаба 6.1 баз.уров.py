import math
x = float(input('Введите ккал на 100гр '))
y = float(input('Введите вес продукта '))
class lon(object):
	"""docstring for lon"""
	def __init__(self, r1, r2):
		self.x = r1
		self.y = r2
	def chet (self):
		self.rast = (self.x*self.y)/100
	def prin (self):
		print ('ккал продукта - ',self.rast)
obj = lon(x,y)
obj.chet()
obj.prin()
		
