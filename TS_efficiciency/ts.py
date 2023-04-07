import bigot
from time import sleep


def on(n):
    x = 100000*"-"*int(n)  # noqa
    sleep(0.001*n)


def on2(n):
    x = 100000*"-"*int(n**2)  # noqa
    sleep(0.001*n**2)



# You can test our fancy options

# Use the Space() and Time() classes to benchmark functions
# Use the Space() and Time() classes to benchmark functions
print("My function has a space complexity of", bigot.Space(on2),
      "and a time complexity of", bigot.Time(on2))
