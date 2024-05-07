#Dictionary is a colletion data type which is unordered and mutable.
mydict = {"name": "Venkat","age": 21,"city": "Bhopal"} #declaration of dictionaries.(:)
print(mydict)

mydict2 = dict(name="Harry",age=23,city="Boston") #The declaration can also be done using this command.(=)
print(mydict2)

value = mydict2["name"] #Accessing the values using the keys.
print(value)

mydict["email"] = "tush@xyz.com" #adding values in the existing dictionary.
print(mydict)

del mydict["name"] #deleting a keyword from a dictionary.
print(mydict)

mydict.pop("age") #used to remove a given keyword.
print(mydict)

mydict2.popitem() #city was removed as it removes the recently added element.
print(mydict2)

mydict3 = dict(name="Vinod",age=31,city="bhopal")
if "name" in mydict3:          #Used for chcking whether the key is inside the dictionary or not.
    print(mydict3["name"])

    try:                        #Used for chcking whether the key is inside the dictionary or not.
        print(mydict3["name"])
    except:
        print("error")

mydict4 = dict(name="Harris",age=43,city="bangalore")  #used for iterating within each element in the entire dictionary.
for key in mydict4:
    print(key)

    for key in mydict4.keys(): #this can be also performed in this way.we can also use values instead of key.
        print(key)

mydict_cpy = mydict4.copy() #This copy function doesnot make changes in the actual dictionary.
mydict_cpy["skills"] = "python"
print(mydict4)
print(mydict_cpy)

my_dict5 = {"name":"John", "age":28,"email":"John@xyz.com"}
my_dict6 = dict(name="mary",age=27,city="boston")
my_dict5.update(my_dict6)    #Merging of dictionaries.
print(my_dict5)


#We used strings as keys in the entire module but we can also use numbers as keys,and also we can use tuples-
#if it contains immutable elements in it.

my_dict7 = {3: 9,6: 36,9:81} #Numbers can be used as keys in dictionaries.
print(my_dict7)

value = my_dict7[3] #we must only use the key(numberic) mentioned or else we cannot access the values.
print(value) #output - 9

mytuple = (8,7)
my_dict8 = {mytuple: 15} #This is possible sincxe tuple is immutable.
print(my_dict8) #output - {(8, 7): 15}

mylist = [8,7]
my_dict9 = {mylist: 15}
print(mylist)  #Output -  my_dict9 = {mylist: 15}
           #    ^^^^^^^^^^^^
#TypeError: unhashable type: 'list'

#Reason - This happened because list is mutable.
