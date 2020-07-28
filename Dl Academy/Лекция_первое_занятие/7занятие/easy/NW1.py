import math

class Triangle:
	def __init__(self, A,B,C):


		def sideLen(dot1, dot2):
			return math.sqrt((dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2)

		self.A = A
		self.B = B
		self.C = C

		self.AB = sideLen(self.A, self.B)
		self.BC = sideLen(self.B, self.C)
		self.CA = sideLen(self.C, self.A)


	def areaTriangle(self):
		semi_perimetr = self.perimetrTriangle() /  2

		return math.sqrt(semi_perimetr * (semi_perimetr - self.AB) * (semi_perimetr - self.BC) * (semi_perimetr - self.CA))

	def perimetrTriangle(self):
		return self.AB + self.BC + self.CA

	def heightTriangle(self):
		return self.areaTriangle() / (self.AB / 2)

treugolnik1 = Triangle((3, 2), (6, 7), (0, 12))

print(treugolnik1.areaTriangle)
print(treugolnik1.heightTriangle)
print(treugolnik1.perimetrTriangle)



			
	
		


