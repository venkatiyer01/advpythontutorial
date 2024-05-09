#String is an ordered and immutable data type which is used for text representation.

my_string = "Hello World"
char = my_string[0] #This is said to be known as string slicing which is similar to lists.(-ve index acceptible)
print(char) #Output - H

substring = my_string[1:5]
print(substring) #Output - ello

Greeting = "Hello"
name = "Tom"
sentence = Greeting + " " + name #Concatenated String.
print(sentence) #Output - Hello Tom

for i in my_string: #Iteration in a string.
    print(i) #Output - All of the elements are printed seperately in a new line.

my_string1 = 'biggest'
if 'e' in my_string1:
    print('Yes')
else:
    print('No')

my_string3 = "     Hello World    "
my_string3 = my_string3.strip() #This inbuilt function removes all the unnecesssary spaces present in it.
print(my_string3)

my_string4 = "hello world"
print(my_string4.upper()) #Ouput - HELLO WORLD Converts every letter to uppercase and similar for lower.
print(my_string4.startswith("hello")) #Output - True
#Checks whether the string starts with the same element or not.
print(my_string4.endswith("world")) #Output - True
#Checks whether the string ends with the same element or not.
print(my_string4.find("o")) #Output - 4
#Tells the index of a particular letter in a string.
#If it finds a string it will give an exact index and if it doesn't then it will print -1.
print(my_string4.count('l'))  #Output-3 #Counts the number of inputted letter in it.
print(my_string4.replace("world","Universe")) #Output - hello Universe
#Replace function replaces the given name with new name given.

my_string5 = "How are you doing?"
print(my_string5.split()) #Output - ['How', 'are', 'you', 'doing?']
#This split functions converts the string into a list.

my_string6 = "How are you doing?"
print(my_string6.split(",")) #Output - ['How', 'are', 'you', 'doing?']
#In order to remove the extra seperators we must add the particular seprator in the split parenthesis in order-
# to form a list.
new_list = ''.join(my_string6) #Combines the elements of list to a string.
print(new_list) #Output - How are you doing?

my_list = 'a' * 6
new_list1 = ''.join(my_list) #Combines the elements of the string.
print(new_list1) #Output - aaaaaa

var = "tom"
my_string7 = "The variable is %s" % var #This function takes the acess of the string variable and prints it.
print(my_string7) #Output - The variable is tom.
var1 = 2
mynum = "the variable is %d" % var1 #this function pints the number assigned to the variable.
print(mynum) #Output - the variable is 2
var2 = 2.1235464
myfloat = "the variable is %f" % var2 #nf to be printed if we want specific number of decimals to be printed.
print(myfloat) #Output - the variable is 2.123546

#New way to do the same thing is::
my_string8 = "The variable is {}".format(var)
print(my_string8) #Output - The variable is tom
mynum2 = "The float value is {:.2f} and {}".format(var2,var)
print(mynum2) #Output - The float value is 2.12 and tom

#f-strings
mynum3 = f"The variables are {var} and {var1}"
print(mynum3) #Output - The variables are tom and 2.
