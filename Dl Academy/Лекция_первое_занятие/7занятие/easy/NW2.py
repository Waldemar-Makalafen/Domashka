class Trapeze:
	def __init__(self, A,B,C,D):
		def sideLen(dot1, dot2):
			return math.sqrt((dot1[0] - dot2[0])**2 + (dot1[1] - dot2[1])**2)

		def areaTriangle(len1, len2, len3):
			semi_perimetr = (len1 + len2 + len3)/2

			return math.sqrt(semi_perimetr * (semi_perimetr - len1) * (semi_perimetr - len2)  * (semi_perimetr - len3) )

		self.A = A
		self.B = B
		self.C = C
		self.D = D

		self.AB = sideLen(self.A, self.B)
		self.BC = sideLen(self.B, self.C)
		self.CD = sideLen(self.C, self.D)
		self.DA = sideLen(self.D, self.A)

		self.diagonal_AC = sideLen(self.C, self.A)
		self.diagonal_BD = sideLen(self.B, self.D)

		self.perimetr = self.AB + self.BC + self.CD + self.DA

		self.area = areaTriangle(self.AB, self.diagonal_BD, self.DA) + areaTriangle(self.diagonal_BD, self.BD, self.DA)

	def eto_trapezz(self):
		if self.diagonal_AC == self.diagonal_BD:
			return True

		return False
		


NW_trapezz = Trapeze(5,3,3)