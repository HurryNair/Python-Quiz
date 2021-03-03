def q1():
	print("hello" * 5)
# 'hellohellohellohello"

def q2():
	x, y = 4, 5
	y, x = x, y
	print(x)
	print(y)
# 5
# 4

def q3():
	z = 9
	lst = [0] * z
	print(lst[:-1])
# 0

def q4():
	def help(x):
		return x % 2 == 0

	lst = [i**2 for i in range(10)]
	# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] 
	lst = filter(help, lst)
	#list(lst) = [0, 4, 16, 36, 64] 
	print(list(lst)[::2])
	# [0, 16, 64]

def q5():
	z = 0
	for i in range(1, 10):
		if (i + 1 // 2) % 7 == 0:
			break
		else:
			z += int(i % 2 == 0)
			print(z)
	else:
		print('end')
	# BODMAS
	# In (i + 1 // 2) floor div happens first
	# i = 1; z = 0
	# i = 2; z = 1
	# i = 3; z = 1
	# i = 4; z = 2
	# i = 5; z = 2
	# i = 6; z = 3 
	# The else block just after for/while is executed only when the loop is NOT terminated by a break statement.

def q6():
	import math

	for i in range(1, 100):
		if math.sqrt(i) == (i - 5)**2:
			print(i)
			break
	else:
		print('no')
	# This can not be true for any value of range(n)
	# no

def q7():
	class A:
		def __init__(self, x):
			self.x = x

		def __eq__(self, o):
			return self.x == o.x

	a = A(2)
	b = A(2)
	print(a == b)
	# a.__eq__(self, b)
	# True
	print(a is b)
	# is compared memory address of objects 
	print(b is a)
	print(a is a)
	print(a == a)

def q8():
	class A:
		def __init__(self, x, y):
			self.x = x
			self.y = y

		def print(self):
			print(self.x, self.y)

	class B(A):
		def print(self):
			print(self.y, self.x)

	class C(B):
		def __init__(self, x, y, z):
			super().__init__(x, y)
			self.z = z

	d = A(2, 4)
	# d.x = 2
	# d.y = 4
	
	e = B(4, 5)
	# Uses init of parent class
	# Uses print of its own
	# e.x = 4
	# e.y = 5

	g = C(3, 4, 7)
	# Utilizes init of parent class &
	# modifies it for 3rd variable
	# simply inherits print from parent (B)
	# g.x = 3
	# g.y = 4
	# g.z = 7
	
	g.x = g.z
	# g.x = 7
	
	d.print()
	# 2 4
	e.print()
	# 5 4
	g.print()
	# 4 7

def q9():
	def x(z):
		def q(x, y):
			x = y + z + x
			print(x)

		return q

	for i in range(10):
		func = x(i)
		# func = q at this point with z = i
		func(i, i-1)
		# th
'''
i = 0
x = 0, y = -1
>> -1

i = 1
x = 1, y = 0
>> 2

i = 2
x = 2, y = 1
>> 5

''' 
def q10():
	def d(f):
		def w(*args, **kwargs):
			r = f(*args, **kwargs) 
			r += 1 
			return r 

		return w

	@d
	def a(x):
		return x + 1

	print(a(5))
# Control flow
# print invokes a
# func a gets passed as f into d since d decorates a
# d tries to return w & invokes it
# w runs f & initiaites & mofies r
# r is returned

def q11():
	print(*list(map(lambda x: chr(ord(x) + 1), ["a", "b", "c"])))
# map() maps arguments to the function
# lambda arguments : expression
# * unpacks list into individual variables

def q12():
	x = 0.1
	y = 0.10000000000000001
	print(x == y)
# True

def q13():
	x = [True, 1, "a", "b", "2"]
	print(any(x)) 
# True

def q14():
	x = ["a", 1, 2, 3, 4]
	y = z = x # shallow copy
	z[1] = 7 # ["a", 7, 2, 3, 4]
	y[3] = 2 # ["a", 7, 2, 2, 4]
	x[2] = 9 # ["a", 7, 9, 2, 4]
	print(x) # ["a", 7, 9, 2, 4]
	print(y) # ["a", 7, 9, 2, 4]
	print(z) # ["a", 7, 9, 2, 4]

def q15():
	print(1 == True) # True
	print("1" == 1) # False

def q16():
	x = b'1001'
	y = b'1010'
	z = x + y
	print(z)
	# b'10011010'

def q17():
	x = 0b1001 # 9
	y = 0b1010 # 10
	z = x + y # 19
	print(z)

