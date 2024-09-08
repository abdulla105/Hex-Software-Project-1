# initiate first two numbers in Fibonacci sequence
a, b = 0, 1
#print first two numbers 
print(a)
print(b)
# use a While loop to generate the Fibonacci Sequence
while True:
    #calculate the next number
    a, b = b, a + b
    print(b)
    