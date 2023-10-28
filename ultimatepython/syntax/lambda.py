# A lambda function is a small anonymous function
# Syntax - lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# Doubling a number using Lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

