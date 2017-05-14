a = float(input('кол-во витамина в 1гр. продукта - '))
b = float(input('вес продукта в граммах - '))
c= int ()
class Class1:
	def __init__(self, c1, c2):
		self.a = c1
		self.b = c2
class Class2 (Class1):
	def __init__(self, c1, c2, c3):
		Class1.__init__(self, c1, c2)
		self.c = c3
	def d(self):
		self.d = self.a*self.b
	def out(self):
		print ("кол-во витамина в продукте -" , self.d)
obj = Class2(a,b,c)
obj.d()
obj.out()
