#Lambda function is a small one liner anonymous function that is defined with an order name.
# Lambda: arguments: expressions
# It can take any number of arguments, but can only have one expression.
# Lambda functions are often used when you need a simple function for a short period of time.

add10 = lambda x: x+10
print(add10(5)) #Output - 15

mult = lambda x,y : x*y
print(mult(5,10)) #Output - 50

points2D = [(1,2),(15,1),(5,-1),(10,1)]
points2D_sorted = sorted(points2D)
points2D_sorted1 = sorted(points2D,key=lambda x:x[1])
print(points2D_sorted) #Output - [(1, 2), (5, -1), (10, 1), (15, 1)]
print(points2D_sorted1) #Output - [(5, -1), (15, 1), (10, 1), (1, 2)]

points2D1 = [(1,2),(15,1),(5,-1),(10,1)]
points2D1_sorted = sorted(points2D1,key=lambda x:x[0] + x[1]) #This sorts the elements according to the sums
print(points2D1_sorted) #Output - [(1, 2), (5, -1), (10, 1), (15, 1)]

# map(func , seq) Takes function as an argument and arranges it in a sequence.
a = [1,2,3,4,5]
b = map(lambda x:x*2, a)
print(list(b)) #Output - [2, 4, 6, 8, 10]
c = [x*2 for x in a] #List comprehension.
print(c) #Output - [2, 4, 6, 8, 10]

#filter(func, seq) - Will return values only for True.
d = [1,2,3,4,5,6]
e = filter(lambda x: x%2==0,d)
print(list(e)) #Output - [2, 4, 6]
f = [x for x in d if x%2==0] #List comprehension.
print(f) #Output - [2, 4, 6]

#reduce(func, seq)
from functools import reduce
g =[1,2,3,4,5,6]
product_g = reduce(lambda x,y:x*y,g)
print(product_g) #Output - 720


