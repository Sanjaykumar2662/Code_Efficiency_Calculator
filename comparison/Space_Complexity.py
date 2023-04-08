from memory_profiler import profile
@profile
def my_func(x):
	#Always use x as input variable
	
	
	ans=x**2
	
	return(ans)
	

if __name__ == '__main__':
	my_func(6)