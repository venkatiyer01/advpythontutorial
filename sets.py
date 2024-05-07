# Set is a collection datab type which unordered and mutable.
#It does not allow duplicate elments.

myset = {1,2,3,1,2}
print(myset) #output - {1, 2, 3}(1,2 are not printed twice as set does not allow duplicates.)

myset1 = set("hello")
print(myset1) #output - {'e', 'l', 'h', 'o'}

myset.add(4) #Element gets added.
print(myset) #Output - {1, 2, 3, 4}
myset.remove(3) #Element removed.
print(myset) #Output - {1, 2, 4}
myset.discard(2) #Element gets discarded.
print(myset) #Output - {1, 4}

#Note: The key diffference between remove and discard is that in case of remove if th element is not there it-
#  gives a type error and in discard if the element is not there it does not give a type error.
myset2 = {2,3,4,5,6,}
myset2.clear() #clears the entire set.
print(myset2) #output - set()

myset3 = {4,5,6,7,8}
myset3.pop() #Removes element from the top of the set.
print(myset3)
myset3.pop()
print(myset3)

myset4 = {2,3,4,5,6,7}
for i in myset4: #Iterates over every element in the set(for-in loop)
 print(i) #Output - Prints every element in a new line.

if 1 in myset4: #For checking whether the element is there in a set or not.
    print("yes")
else:
    print("no")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8}
primes = {2,3,5,7}
u = odds.union(evens) #This function performs union amongst two sets without duplication.
print(u) #Output - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

i = odds.intersection(evens) #This function performas the intersection amongst both sets.
print(i) #output - set()
#Reason - As there is thing common amongst the sets.
p = odds.intersection(primes)
print(p)#Output - {3, 5, 7}

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB) #Seperates the elements which are not in setA. output - {4, 5, 6, 7, 8, 9}.
print(diff)

symdiff = setA.symmetric_difference(setB) #This function leaves no common elements and make it as a set.
print(symdiff) #Output - {4, 5, 6, 7, 8, 9, 10, 11, 12}.

setA.update(setB) #Updates the elements of B in A.
print(setA) #output - {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

setC = {4,5,6,7}
setD = {5,6,7,8}
setC.intersection_update(setD) #Updates only the common element in both of these.
print(setC) #Output - {5, 6, 7}

setE = {1,2,3,4,5}
setF = {3,4,5,6,7}
setE.difference_update(setF) #Updates the difference amongst both the sets.
print(setE) #Output - {1, 2}

setG = {2,3,4,5}
setH = {3,4,5,6}
setG.symmetric_difference_update(setH) #Updates the symmetric differnce in the first set.
print(setG) #Ouput - {2, 6}

setI = {1,2,3,4,5}
setJ = {1,2,3}
print(setI.issubset(setJ)) #Tells whether a set is a subset of another  #Ouput - False
print(setI.issuperset(setJ)) #Tells whether a set is a superset of another. #Output - True
# (.issuperset - A set is said to be known as a supeset if setI contains all the elements which are present in-
#                                                                                                        setJ.
print(setI.isdisjoint(setG)) #Output - False
#Disjoint returns true if both sets have null intersection.

setK = setJ.copy() #Does not make changes in the original set.
setJ.add(21)
print(setK) #Output - {1, 2, 3}
print(setJ) #Output - {1, 2, 3, 21}

a = frozenset([1,2,3,4]) #If we declare this as a frozen set we cant add or remove an element afterwards.
a.add(2)
#print(a) #File "D:\tutorials\sets.py", line 91, in <module>
 #   a.add(2)
  #  ^^^^^
# AttributeError: 'frozenset' object has no attribute 'add'.

#Note - In frozen Union,intersection and difference method works.