#lists and loops
a = ['Chelsea', 'Kimberley', 'Arup', 'Christopher', 'Sherine', 'Mason', 'Devikala', 'Drew', 'Somayeh', 'Melpomeni', 'Siyoung', 'Shennon', 'David', 'Ryan', 'Naisarg', 'Maria', 'Mohammad', 'Rachel', 'Daron', 'Kat', 'Kelsey', 'James', 'Maggie', 'Saad', 'Aditi', 'Brigette', 'Jaira', 'Christopher', 'Gernot', 'Taylor', 'Vasilisa', 'Sureshbabu', 'Thomas', 'Tejpal', 'Mahesh', 'Jakob', 'Victoria', 'Brian', 'Dakota', 'Jiman', 'Lauren', 'Billy', 'Jesse', 'John', 'Veronica', 'Kyle', 'Michael', 'Hassan', 'Mathew', 'Ida', 'Irina', 'Chen', 'Margaret', 'Timothy', 'Yiquan', 'Renbin', 'Erik']

print len(a) #lists have length
print type(a) #a
print a[0] #you can index
print type(a[0]) #a is a list of strings
print a[0].count('e')#string methods are available on strings within your lists
print range(len(a)) #range function often used for indexing into arrays
print type(range(len(a))) #also a list

#range generates a list
#the elements of the list contain index into an array

for i in range(len(a)):
    print a[i]



lengths = [] #you can initialize an empty array
for i in range(len(a)):
    l = len(a[i])
    lengths.append(l) #what's this?


#this loop goes through
print lengths
print len(lengths)
len(lengths) == len(a)
###divide into groups and try to calculate the sum of the lengths, start by writing psuedo or talking about the necessary components

print lengths[-1] #print last element in lengths
print a[-1] # should make sense
lengths[-1] = 50
print lengths[-1] #you can change the value held at any index
print a[0][3] #you are now indexing into the string at the first element in the list
a[0][3] = 'a' #uh oh, remember strings aren't mutable
###but what if we want to operate on strings, and make changes?\
string_a = ''.join(a) #this is how you take a list a
print string_a #

nonsense_string = "asdfhao83nml29rj`1o29p3wflmudabio8a9lw3finevqaslvrghi8qn4eruav"

###divide into groups again and
#0.) find out how many instances of the string 'a' are in the nonsense string using the count method
#1.) use the split method to turn nonsense_string into a list, removing all instances of the string 'm'
#2.) go to the first element in your new list, change the 3rd value of this element to '9'
#3). add the string "listsarerad" to the end of the list
#4). now that we've made some changes, calculate how many instances of the string 'a' are in your list using the count method
#5). turn it back into a string


#sets are uniqe versions of lists, meaning they contain only unique entries
len(a)
set(a)
len(set(a)) #looks like we've got some duplicate name(s) in the class
la = list(set(a))

for i in range(len(set(a))):
    print i

#sets are not iterable

###while loops

g = list(nonsense_string)
lg0 = len(g)
c = 0
while c < 10:
    del(g[-1])
    c+=1 #fancy way of just saying c = c + 1

lg1 = len(g)
lg0 - lg1
#lost 10 elements

##########a few nifty methods with lists

a #beloved class
a.reverse() #backwards
print a

x = [3, 4, 5, 12, -3]
min(x)
max(x)
sum(x)
x.sort()

print x
