import random
import big_o
def function(x):
	#Always use x as input variable
	
	
	se=x**2
	
	return(se)
def positive_int_generator(n):
	return random.randint(0, 10000)
best, others = big_o.big_o(function, positive_int_generator, n_repeats=50)
print(best)