import time
from functools import reduce

class Prime:
	
 
	def __init__(self):
		"""Constructor"""
		pass

	def is_prime(self, i):
		for j in range (2, i):
			if (i%j==0):
				return False
		return True		 


	def timer(f):
		def temp(self, arg):
			before = time.time()
			result = f(self, arg)
			print ('Время выполнения функции в микросекундах:')
			dif=time.time()-before
			print (dif/1000000)
			return result
		return temp


	def check(self, num):
		if not num.isdigit() or (int(num)==0 or int(num)==1):
			return False
		return True


	@timer
	def get_primes(self, num):
		return [i for i in range(2, num+1) if self.is_prime(i)]


if __name__ == '__main__':
	inst=Prime();
	num = input()
	if not check(num):
			print ('Введите целое положительное число, большее 1')
			exit(1)
	primes = reduce((lambda x, y: str(x) + ', '+ str(y)), inst.get_primes(int(num)))
	print(primes)

		