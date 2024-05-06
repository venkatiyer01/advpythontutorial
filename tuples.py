#Tuples is similar to lists but the main difference between these two is that, a tuple cannot be changed after -
#it is created or Tuple is immutable.
mytuple0 = ("mix" , 35 , "jelly") #tuple is created inside a () ![].
mytuple = tuple(["max" , 28 , "botson"]) #Convrsion of list to tuple.
print(type(mytuple))

item = mytuple[1] #Both positive and negatve indexing works in this case.
print(item)

# mytuple[0] = "Tim" #Since tuuple is immutable assignment cannot be done.

for i in mytuple:
    print(i) #output - All three printed
#print(2*i) output - All thre printed but 2*i times.

if "max" in mytuple: #if else in mytuple works fr.
    print("yes")
else:
    print("no")

my_tuple = ('a','p','p','l','e') #Prints the length of my tuple.
print(len(my_tuple))

print(my_tuple.count('p')) #counts the number of identical elements.
print(my_tuple.index('a')) #prints the indexing of specific element.

my_list = list(my_tuple)
print(my_list)
my_tuple2 = tuple(my_list)
print(my_tuple2)
#Both list and tuple can be converted to each other using list and tuple functions.

a = (1,2,3,4,5,6,7,8,9)
b = a[2:5] #slicing can be done in both positive and negative indexing.
print(b) #output - (3, 4, 5)
c = a[1:8:2] #in this case the last index gets printed.Output - (2, 4, 6, 8)
print(c) #output - (2, 4, 6, 8)
d = a[::-1] #reverses the entirre tuple.
print(d)

my_tuple3 = "jimmy" , 32 , "Brazil"  #no () required.
name , age , place = my_tuple3 #assignment of vriables.
print(name)
print(age)
print(place)

my_tuple4 = (0,1,2,3,4,5,6,7,8)
*i1 , i2 , i3 = my_tuple4
print(i1) # '*' creates a list of elements.
print(i3)
print(i2)


#Comparison in terms of list and tuples.
# 1. Tuple < list in terms of size,which states that it acquires lesser space in the memory.
# 2. Tuple < list in terms of time, which tells us that it takes lesser time to execute programs and generate-
#                                                                                                    outputs.