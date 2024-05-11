#Itertools is a module is collection of tools for handling iterators.Data types which are used in for loop
#Itertools: Product,Permutations,Combinations,accumulate,groupby, and infinite iterators.
from itertools import product
a = [1,2]
b = [3,4]
prod = product(a,b) #Performs the cartesian product.
print(list(prod)) #Output - [(1, 3), (1, 4), (2, 3), (2, 4)]
c = [3]
prod2 = product(a,c,repeat=2) #Repetation.
print(list(prod2)) #Output - [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

from itertools import permutations
c = [1,2,3]
perm = permutations(c) #Gives different orderings of a list this is what permutation is.
print(list(perm)) #Output - [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

from itertools import permutations
d = [3,4,5]
perm1 = permutations(d,2) #Gives different ordrings of a list as per the given list.
print(list(perm1)) #Output - [(3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4)]

from itertools import combinations,combinations_with_replacement
#The combinations are functions will make all possible combination swish a specifid length.
c = [1,2,3,4]
comb = combinations(c,2)
print(list(comb)) #Output - [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
comb_wr = combinations_with_replacement(c,2) #Replacement application repeats the elements.
print(list(comb_wr)) #Output - [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

from itertools import accumulate
d = [1,2,3,4]
acc = accumulate(d) #Uses the pattern (x1,x2+x1,x3+x2+x1,x4+x3+x2+x1)
print(d)
print(list(acc)) #Output - [1, 3, 6, 10]

from itertools import accumulate
import operator
d = [1,2,3,4]
acc1 = accumulate(d,func=operator.mul) #for function using accumulator inside a list.
print(list(acc1))

from itertools import accumulate
import operator
e= [1,2,5,3,4]
acc2 = accumulate(e,func=max) #Prints the maximum of all numbers in the list.
print(list(acc2)) #Output - [1, 2, 5, 5, 5]

#Groupby function make an iterator that returns keys and groups from a iterable.
from itertools import groupby

def smaller_than_3(x):
   return x < 3

f = [1,2,3,4]
group_obj = groupby(f, key=smaller_than_3)
for key,values in group_obj:
 print(key, list(values)) #Output - True [1, 2] False [3, 4]

from itertools import count,cycle,repeat
for i in count(10):
    print(i) #Output - Starts counting from 10 till infinity...
    if i==15:
        break #breaks here and stops the count as per this.

from itertools import count,cycle,repeat
g = [1,2,3]
for i in cycle(g): #Output Will print 1 2 3 1 2 3 until I make a stop condition.
    print(i)
    if i == 3:
        break

from itertools import count,cycle,repeat
h = [1,2,3]
for i in repeat(1,4):
    print(i) #Output - Prints 1 for 4 times.

    


