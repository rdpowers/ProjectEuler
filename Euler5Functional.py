def gcd(a,b):
	if(b==0):
		return a
	else:
		return gcd(b,a%b)

def main():
	upperbound=20
	nums=range(1,upperbound+1)
	print reduce(lambda n,m:n*(m/gcd(n,m)),nums)
	

if __name__ == '__main__':
	status = main()
#	print status