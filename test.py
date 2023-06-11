txt ="We are the so called \"vikings\" from the north"
print(txt)
playlist=["monday,tuseday,wednesday"]
playlist.insert(3,"thursday")
print(playlist)
weekend=["saturday,sunday"]
playlist.extend(weekend)
print(playlist)
a=33
b=4
if a<b:
    print("a is less than b")
else:
   print("a is not lesser than b")
print(bool(None))

x=10

def myfunc():
   x=15   
   print("python is",x);

myfunc()
thislist=["tameera,donde,kaendi"]
thislist.insert(2,"hilmara")
print(thislist)
thistuple=('chris','teresa')
thislist.extend(thistuple)
print(thislist)
thislist.clear()
print(thislist)
#looping using while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

thislist2=["tameera","kaendi","sussana"]
i=0
while i < len(thislist2):
   print(thislist2[i])
   i=i+1
   
   fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist3 = [x for x in fruits if "a" in x]

print(newlist3)

b=[1,2,-7,-9]
print(b)
b[1]="tameera"
print(b)
c=b[0:2]
print(c)
#learnt the difference between copying(:)
#  and duplicate(c=b)the values of c and b will change if either is changed in duplicate 
# but in copying the original value remains the same(khan academy)
c=b#duplicate
A=b[:]#copying
print(b,A)
b[1]="jemmy"
print(c,A)
b[1]=1
b.sort()
print(b)

#tuples
thistuple=("tameera,")
print(thistuple)
#datatype of tuple is tuple


#to find an item in a tuple use if statement,also indentation is very important in if statements
mytuple=("x","y","z")
if "x" in mytuple:
   print("ye,'x' is in this tuple")

#workaround of adding items on tuple which are unchangable
#just change the tuple into a list add the item and change it back
x=list(mytuple)
print(x)
x.insert(3,"m")
print(x)
mytuple=tuple(x)
print(mytuple)

x=list(mytuple)
x.remove("m")
mytuple=tuple(x)
print(mytuple)

#looping through tuples
#using for
for x in mytuple:
   print(x)

#using while loop


#sets
thisset={"apple","mango",True,1}
print(thisset)
print(type(thisset))
#sets can also be created by double quotes

#looping through sets
for x in thisset:
   print(x)

#finding a value in aset
if "apple" in thisset:
   print("yes,'apple'is in this set")
   
#you can add lists and other iterable objects to a set by
thisset.update(thislist2)
print(thisset)

#joining sets
thisset2={"mon","tue","apple","mango"}
print(thisset2)
thisset3=thisset.union(thisset2)
print(thisset3)
#reminder sets are not ordered

thisset2.update(thisset)

#how to keep the items that are present in both sets
thisset.intersection_update(thisset2)
print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#sets{},lists[],tuples(),dictionaries{}....TO NOTE


#Dictionaries
thisdict ={
   "name":"tameera",
    "gender":"female",
    "age": 22,
   "student": True
}
print(thisdict)

#to get value of a key
x=thisdict["name"]
print(x)

y=thisdict["gender"]
print(y)

#to get all values in the dict

x=thisdict.values()
print(x)

#to change values in a dict
thisdict["gender"]="male"
print(x)

#looping

for x in thisdict.items():
   print(x)

for x in thisdict.keys():
   print(x)

for x in thisdict.values():
   print(x)

#nested dict
thisdict2 ={
   "name":{
      "firstname":"tameera",
      "secondname":"donde"
  },
   "age":{
      "dob":2000,
      "month": "october",
      "date": 22
   },
   "gender": "female"
 }
print(thisdict2)

#to get nedsted dict from main dict
print(thisdict2["name"]["firstname"])

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(myfamily["child1"]["name"])
print(myfamily["child2"]["year"])
#remember to use square brackets and quations when seeking out nested dict

#if statements
a=18
b=12
if a>b:
   print("a is greater than b")
elif a<b:
   print("a is lesser than b")
else:#else doesnt have to have a condition
   print("a is equal to b")

#putting if statements in one line(start with print then if )
c=18
d=18
print("they equal") if c==d else print("c is less than d") if c<d else print("c is greater than d")

#nested if statements
if c>20:
   print("greater than 20")
   if c>30:
      print("greater than 30 too")
else:

   print("not greater than either")

if c==d:
   pass


if a == b or c == d:
  print("Hello")

#looping
#while loop where we can excecute a set of statements as long as the condition is true

e=1
while e<=6:
  print(e)
  e+=1 #remember to increment or else the code will continue forever(zzzzzzz)
  if e==4:
   continue #statements such as break,continue etc have no colons at the end
   print(e)

   


def myfunct2(fname):
      print(fname+ " donde")

myfunct2("tam")






def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") 

def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#indexes start at 0
def myfunct3(*mychild):
   print(mychild[1] + "is a girl")
myfunct3("tameera","jemmy")




#we can use the = to tell the 
def myfunct4(child1,child2,child3):
   print("my childs name is "+child2)
myfunct4(child1="jemmy", child2="tam", child3="gift")



def myfunct5(foods):
   for x in foods:
      print(x)

foods=["mango","meat","sphagetti"]
myfunct5(foods)



def myfunct6(classes):
   for x in classes:
      print(X)

   classes=("maths","english","science")
   myfunct6(classes)


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11)











 






