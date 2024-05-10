#Collections are basically container data types.
#Collections : Counter,namedtuple,ordereddict,defaultdict and deque.

from collections import Counter
a = "aaaaabbbbcccc"
my_counter = Counter(a) #Creates a dictionary by counting the number of identical characters in a string.
print(my_counter) #Output - Counter({'a': 5, 'b': 4, 'c': 4})
print(my_counter.values()) #Output - dict_values([5, 4, 4])
print(my_counter.items()) #Output - dict_items([('a', 5), ('b', 4), ('c', 4)])
print(my_counter.keys()) #Output - dict_keys(['a', 'b', 'c'])
print(my_counter)
print(my_counter.most_common(2)) #Output - [('a', 5), ('b', 4)]
#Prints the list with tuples with the most common elements in the dictionary.
print(my_counter.most_common(1)[0]) #Output - ('a', 5) (Returns a tuple.)
print(my_counter.most_common(1)[0][0]) #Output - a  (Returns the most common element)
print(list(my_counter.elements())) #Output - ['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c']

#Namedtuple - This is an easy to create and lightweight objecttype such as struct.

from collections import namedtuple
point = namedtuple('point','x,y') #Creates a class named point.
pt = point(1,-4) #Assigns a value to it.
print(pt) #Output - point(x=1, y=-4)
print(pt.x,pt.y) #Output - 1 -4

#Ordereddict is just like a normal dictionary but it remembers the order in which the elements were stores.
from collections import OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict) #Output - OrderedDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})

ordered_dict1 = {}
ordered_dict1['b'] = 2
ordered_dict1['c'] = 3
ordered_dict1['d'] = 4
ordered_dict1['a'] = 1
print(ordered_dict1) #Output - {'b': 2, 'c': 3, 'd': 4, 'a': 1}

from collections import defaultdict
d = defaultdict(int) #We can set thi sto anything such as list,float,etc etc...
d['a'] = 1
d['b'] = 2
print(d['a']) #Output - 1
print(d['c']) #Output - 0
#This will print a default value if the key doesn't exists.

#Deque is a double ended queue it can be used to add and remove elements from both ends and both are implemented in-
# a way that thi swill be very efficient.
from collections import deque
d2 = deque()
d2.append(1)
d2.append(2)
print(d2) #Output - deque([1, 2])

d2.appendleft(3)
print(d2) #Output - deque([3, 1, 2])

d2.pop()
print(d2) #Output - deque([3, 1])

d2.popleft()
print(d2) #Output - deque([1])

d2.clear()
print(d2) #deque([])

d2.extend([4,5,6])
print(d2) #Output - deque([4, 5, 6])

d2.extendleft([7,8,9])
print(d2) #Output - deque([9, 8, 7, 4, 5, 6])

d2.rotate(1) #Rotates elements n places to the right.
print(d2) #Output - deque([9, 8, 7, 4, 5, 6])





