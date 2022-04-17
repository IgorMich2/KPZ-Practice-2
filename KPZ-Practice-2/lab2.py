import math

last = 1

def prime_num_generator():
	global last
	last = nextPrime(last)
	print(last)

def isPrime(n):
	if(n <= 1):
		return False
	if(n <= 3):
		return True
	
	if(n % 2 == 0 or n % 3 == 0):
		return False
	
	for i in range(5,int(math.sqrt(n) + 1), 6):
		if(n % i == 0 or n % (i + 2) == 0):
			return False

	return True

def nextPrime(N):
	if (N <= 1):
		return 2

	prime = N
	found = False

	while(not found):
		prime = prime + 1

		if(isPrime(prime) == True):
			found = True

	return prime

i=1
for i in range(100):
	prime_num_generator()