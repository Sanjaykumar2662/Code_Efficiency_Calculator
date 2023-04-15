from memory_profiler import profile
@profile
def my_func(x):
	#Always use x as input variable
	
	
	sq=x**2
	
	return(sq)
	

if __name__ == '__main__':
	my_func(6)