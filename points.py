import matplotlib.pyplot as plt

class Point:
	def __init__(self, x,y, color="red", size=10):
		self.x = x
		self.y = y
		self.color = color
		self.size = size

	def __add__(self, other):
		if isinstance(other, Point):
			x = self.x + other.x
			y = self.y + other.y
			return Point(x,y)
		else:
			x = self.x + other
			y = self.y + other
			return Point(x,y)

	def plot(self):
		plt.scatter(self.x, self.y, c=self.color, s=self.size)

if __name__ == "__main__":
	a = Point(1,3)
	b = Point(2,4)
	c = a + b
	c.plot()
	plt.show()