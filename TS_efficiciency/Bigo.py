from big_o import BigO

def my_function(n):
    for i in range(n):
        print(i)
        
analysis = BigO()
time_complexity = analysis.time_complexity(my_function)
space_complexity = analysis.space_complexity(my_function)

print("Time complexity:", time_complexity)
print("Space complexity:", space_complexity)
