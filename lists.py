mylist = ["banana", "cherry" , "apple"]
print(mylist)

mylist0 = list() #we can also create an empty list and it will get printed either.
print(mylist0)


mylist2 = [5 , True , 'string']  #list can contain integer, boolean, and string.
print(mylist2)

item = mylist[1]  #accessing the elements from the list using indexing.
#We can also use negative indexing along with this -1 specifies the last element in the list.
print(item)

for i in mylist:
    print(i) #If I want to iterate over my entire list we will be using for in loop.
#We can also use use other variable other than i.

if "lemon" in mylist: #we  use this in order to check whether the eement is available in it or not.(if not If)
    print("yes")  #there should be some spaces available at the start in order to avoid errors.
else:
    print("no")

print(len(mylist)) #length of the list.
mylist.append("lemon") #inserting a new element at the end of the list.
print(mylist)

mylist.insert(1, "blueberry") #used for adding a new elemtn in a specific position in a list.
print(mylist)

item1 = mylist.pop() #removes the last element from the list.
print(item1)
print(mylist)

item2 = mylist.remove("cherry") #for removing an elementr from any random place in a list.
print(mylist)

item3 = mylist2.clear() #as the name suggests gives an empty list.
print(mylist2)

item4 = mylist.reverse() #reverses the order of elements from a particular list.
print(mylist)

mylist3 = [4,3,1,-1,-5,10] #sorts the elements in ascending order.
item5 = mylist3.sort()
print(mylist3)

mylist4 = [2,3,-1,4,10,13]
new_list = sorted(mylist4) #Here sorted is a function which we can use in other iterables to such as tuples n strings.
print(mylist4)
print(new_list)

mylist5 = [0] * 5
print(mylist5)
mylist6 = [1,2,3,4,5]
new_list1 = mylist5 + mylist6
print(new_list1)

mylist7 = [1,2,3,4,5,6,7,8,9]
# a=mylist7[1:5] #last index gets excluded in ths slicing.
# print(a)  output = [2,3,4,5]
#if we don't specify the start index it starts from the beginning.
#if we don't specify the last index then it goes all the way to the end of the list.

# a= mylist7[::2] #takes every second item.
#print(a) output = [1,3,5,7,9]
#b = mylist[::-1]
#print(b) #output[9,8,7,6,5,4,3,2,1]

list_org = ["banana" , "cherry" , "apple" ]
list_cpy = list_org.copy()

list_cpy.append("lemon") #this will not make changes in the original list.
print(list_org) # output = ['banana' , 'cherry' , 'apple']
print(list_cpy) #output = ['banana' , 'cherry' , 'apple','lemon' ]

list_cpy1 = list_org[:] #this also makes an actual ccopy of this thing(slicing).
print(list_cpy1)

#list comprehension(***)
d = [1,2,3,4,5,6]
e = [i*i for i in d] #can also use other variable nstead of i.
print(d)
print(e)

f = [i for i in d]
print(d)
print(f)