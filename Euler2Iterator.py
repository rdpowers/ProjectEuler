def FibItr():
	a,b = 0,1
	yield a
	yield b
	while True:
		a,b = b, a+b
		yield b
	
if __name__ == '__main__':
	s = 0
	for i in FibItr():
		if i > 4000000:
			break
		if i %2==0:
			s +=i
	print s