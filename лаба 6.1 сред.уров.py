a = int(input('введите часы - '))
b = int(input('введите минуты - '))
c = int(input('введите секунды - '))
class Cl:
	def __init__(self, c1, c2, c3):
		self.a = c1
		self.b = c2
		self.c = c3
	def vrem(self):
		self.vrem = self.a*3600+self.b*60+self.c+5
	def out(self):
		print ("Время в секундах, с учетом + 5 доп.сек - ", self.vrem)
	def __del__(self):
		print ()
obj = Cl(a,b,c)
obj.vrem ()
obj.out ()
del Cl
