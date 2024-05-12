x=-5
 #if x<0:
#    raise Exception('x should be positive')  #Output - Traceback (most recent call last):
 # File "D:\tutorials\python\exceptions_and_errors.py", line 3, in <module>
  #  raise Exception('x should be positive')
#Exception: x should be positive

#assert(x>=0) ,'x is not positive' #Output - Traceback (most recent call last):
#  File "D:\tutorials\python\exceptions_and_errors.py", line 8, in <module>
 #   assert(x>=0) ,'x is not positive'
#           ^^^^
#AssertionError: x is not positive

try:
    a = 5/0
except:
    print("An error happened") #Output -An error happened
    #The program won't stop here for obvious.

    try:
        b= 7/0
    except  Exception as e:
        print(e) #Output - division by zero
    #The program won't stop here for obvious.

