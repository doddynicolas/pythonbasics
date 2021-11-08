from random import randint
N = randint(0, 11)
squareOfSum = 0
sumOfSquare = 0
s = 0
l = []
for i in range(N):
    l.append(i)
    sumOfSquare += (i**2)
    s +=i

squareOfSum += (s**2)
print(l)
print(f"diff = {squareOfSum - sumOfSquare}")
print(f"N = {N}")
print(f"sum of square =  {sumOfSquare}") 
print(f"square of sum =  {squareOfSum}")   

 