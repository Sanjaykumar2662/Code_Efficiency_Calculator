import random
import big_o
def function(x):
	#use input box to give inputs 
	
	#Always use x as input variable
	
	
	return(x**2)
def positive_int_generator(n):
	return random.randint(0, 10000)
best, others = big_o.big_o(function, positive_int_generator, n_repeats=50)
print(best)