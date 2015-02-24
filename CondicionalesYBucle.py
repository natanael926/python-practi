class CondicionalIf(object):

	def __init__(self, num_r):
		self.num = num_r;

	def mensaje(self):

		if(self.num < 0):
			return "Numero es menor que 0"

		elif(self.num > 10):
			return "Numero es mayor que 10"

		else:
			return "Numero estan entre 0 y 10"

# Ci = CondicionalIf(10)
# print Ci.mensaje()


class Bucles(object):
	"""docstring for Bucles"""
	def __init__(self, list_r):
		self.list = list_r;

	def bucleFor(self):
		for i in self.list:
			print i;

	def bucleWhile(self):
		i = 10

		while i < 20:
			print i
			i += 1



list = [1,3,5,7,9]

bu = Bucles(list)
#bu.bucleFor()
bu.bucleWhile()

		
