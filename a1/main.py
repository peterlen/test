import traceback

class Dog:
	"""Dog class description"""

	def __init__(self, tt):
		self.fav = "bones"
		print "In Dog constructor"

	def __str__(self):
		return "Hello there: " + self.fav

	def myName(self):
		print "Zambo"

def main():
	print "Dog class desc: ", Dog.__doc__
	dd = Dog("Collie")
        print dd
        dd.myName()

try:
   main()
except Exception, e:
   traceback.print_exc()
