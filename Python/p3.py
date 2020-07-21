class Complex(object):
	def __init__(self,real,im):
		self.r=real
		self.i=im

	def display(self):
		if self.i>0:
			if self.r!=0:
				print(str(self.r)+'+'+str(self.i)+'i')
			else:
				print(str(self.i)+'i')
		elif self.i==0:
			print(str(self.r))
		else:
			if self.r!=0:
				print(str(self.r)+'-'+str(-(self.i))+'i')
			else:
				print('-'+str(-(self.i))+'i')

	def add(self,c):
		sum_r=self.r+c.r
		sum_i=self.i+c.i
		return Complex(sum_r,sum_i)

	def subtract(self,c):
		diff_r=self.r-c.r
		diff_i=self.i-c.i
		return Complex(diff_r,diff_i)

	def modulus(self):
		return self.r**2+self.i**2

	def multiply(self,c):
		m_r=(self.r*c.r)-(self.i*c.i)
		m_i=(self.r*c.i)+(self.i*c.r)
		return Complex(m_r,m_i)

	def conjugate(self):
		return Complex(self.r,-self.i)

	def inverse(self):
		in_r=self.r/float(self.modulus())
		in_i=-self.i/float(self.modulus())
		return Complex(in_r,in_i)

	def divide(self,c):
		return self.multiply(c.inverse())


#examples
a=Complex(2,4)
a.display()
a.conjugate().display()
a.add(a.conjugate()).display()
a.subtract(a.conjugate()).display()
print('mod',a.modulus())
a.multiply(a.conjugate()).display()