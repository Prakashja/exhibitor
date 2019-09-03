from typing import Set

print('hello world')
print('new line')

a=2+1

print(a)
print("hello")

print("hello \tworld")

mystring = "Hello world"

print(mystring)

print(mystring[7])

print(mystring[-2])

print(mystring[1:])
print(mystring[4:])

print(mystring[4:8])

print(mystring[:3])

myname = "sananaaz"

print(myname[4:])

print(myname[:4])

print(myname[3:6])

print(myname[0:4])

print(myname[::3])

print(myname[::-1])

print(len(myname))

print(myname[2:6:2])

print(myname[::1])



## immutability

name = "sananaaz"

first_name = name[0:4]

print(first_name)

full_name = 'pakash' + first_name

print (full_name)

x = 'hello world'

x = x + " its beautifule out side"

print(x)

letter = 'z'

print(letter * 10)


x = "hello world"

print(x.upper())

print(x.lower())


print(x.split('l'))

print(x.split('o'))

print(x[::1])



myname = "prakash"

print("my name is {}".format(myname))

mylove = "sana"

print ("my name is {1} {0}".format("praksh","sana","naaz"))

print(f"hello my love name is {mylove}")

myresult = 100/777

print(myresult)

print("my result is {0:2.5f}".format(myresult))


name="sana"
age = 23

print(f"{name} is {age} of old")

print("{} is {} of old".format(name,age))



my_list = [1,2,3,4,5]

print(len(my_list))

new_list = ["one","two","three"]
another_list = ["four","five"]

print(new_list + another_list)

new_list[0] = 'one pluse'

print(new_list + another_list)
another_list.append("six")
print(another_list)
another_list.pop()

print(another_list)

print(my_list)

new_list = ["a","b","c","d"]
num_list = [4,8,2,1]

num_list.sort()
num_list.reverse()

print(num_list)

print(type(num_list))


my_dist = {"name":"jai","her":"sana"}

print(my_dist['name'])

prices_lookup = {"apple":20,"orange":20,"mango":00}

print(prices_lookup["apple"])

print(prices_lookup["orange"])

d = {'k1':20,'k2':[1,2,3],"k3":{'insde':20}}

print(d["k3"])
print(d["k2"][2])

d = {'key1':['a','b','c']}

y = d["key1"][2].upper()

print(d["key1"][2].upper())

d["key2"]=200

print(d)

print(d.keys())

print(d.values())

print(d.items())


### tuples immutable

t = (1,2,3,2,2)

print(type(t))

print(t[0])

print(t.count(2))
print(t.index(2))

## sets

myset: Set[int] = set()

myset.add(2)
myset.add(3)
myset.add(1)
mylist = [1,1,1,1,1,3,3,3,3,4,4,4,4]
print(myset)

print(set(mylist))

### boolens

a = 1 > 2
a = 1 == 1

### i/o basic file

myfile = open('myfile.txt')

print(myfile.read())

print(myfile.seek(0))

print(myfile.readline())

print(myfile.close())

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('myfile.txt',mode='a') as f:
     f.write("four on fourth")

x = open('test.txt',mode='r+')
x.write('Hello World')
print(x.read())

####################################################




print ((60 + (10 ** 2) / 4 * 7) - 134.75)


print(4 * (6 + 5) )
print(4 * 6 + 5)
print(4 + 6 * 5)

print(type(3+1.5+4))

print((2 ** 2)/2)

s = "hello"

print(s[1])
print(s[::-1])

print(s[4:])

print(s[-1])

print([0] * 3)

list3 = [1,2,[3,4,'hello']]
list3[2][2] = 'goodbye'
print(list3[2][2])

list4 = [5,3,4,6,1]

list4.sort()
list4.reverse()
print(list4)

d = {'simple_key':'hello'}

print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'

print(d['k1']['k2'])

# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d['k1'][0]['nest_key'][1][0])

# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

print(d['k1'][2]['k2'][1]['tough'][2][0])

t = (1,2,'stupid')

print(t)

list5 = [1,2,2,33,4,4,11,22,3,3,2]

print(set(list5))

print(3.0 == 3)

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

print(l_one[2][0] >= l_two[2]['k1'])


print(1 < 2 and 2>3)

print(not 1 ==2)


########## if elif  else

if 1 == 2:
    print("condition is tru")
elif 1==3:
    print("condition is true")
else:
    print("condition is false")

done = True

if done:
    print("good work!")
else:
    print("do it again")

location = "thumkuras"

if location == "thumkur":
    print("about to reach bengaluru")
elif location == "bengaluru":
    print("reached bengaluru")
else:
    print ("yet to reach")

##### for loop

my_iterable = [1,2,3,4]
for item_name in my_iterable:
    print(item_name)

numlist = [1,2,3,4,5,6,7,8,9,10]

for jelly in numlist:
    print("hello")

for num in numlist:
    ### check for odd numbers
    if num % 2 != 0:
        print(num)
    else:
        print(f"even number: {num}")

list_sum = 0

for num in numlist:
    list_sum = list_sum + num

    print(list_sum)

my_string = "sana naaz"

for string in my_string:
    print(string + "prakash")

tuple = [(1,2),(3,4),(5,6),(7,8)]

for _ in tuple:
    print(_)

for (a,b) in tuple:
    print(a)
    print(b)

d = {'k1':1,'k2':2,'k3':3}

for key,value in d.items():
    print(value)

weekday = True
vacation = True

def sleep_in(weekday, vacation):

    if not weekday or vacation:
        return True
    else:
        return False

#### while loop

x = 0

while x < 5:
    print(f'the current value of {x}')
    x = x + 1
