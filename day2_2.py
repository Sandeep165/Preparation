#data type
'''
List  = [1,2,3,"name"]
set = {1,2,3,"name"}
tuple =  (1,2,3,"name")
dict = {key:value }
{"name":"jack","age":21}
'''


list1 = [1,2,3,"name",True,["python",[[11,22,33,["India"]],"Mumbai","Pune"],"java"],False]

#11,22,India,["India"],Pune,Java
# print(list1[5][1][0][1])
# print(list1[5][2])
# print(list1[5][0][1])
# print(list1[5][0][3][0])
# print(list1[5][0][5])
# print(list1[5][1])
list2 = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', 'h',[[111,222,333],["India"]],["mumbai"],[["Python",245,658,44,10.0]]]

'''
bb
ddd
ee
h
[111,222,333]
333
["India"]
India
Mumbai
python
10.0
["Python",245,658,44,10.0]
'''
# print(list1[5][0])
# print(list1[4])
# print(type(list1))

# print(list2[1][0])
# print(list2[1][1][1])
# print(list2[1][2])
# print(list2[3])
# print(list2[4][0])
# print(list2[4][0][2])
# print(list2[4][1])
# print(list2[4][1][0])
# print(list2[5][0])
# print(list2[6][0][0])
# print(list2[6][0][4])
# print(list2[6][0])
'''
List:
mutable
ordered
allows duplication
it is capable to hold multiple data types

'''

# To add the data
list3 = ["apple","mango","banana"]
# print(list3)
# list3.insert(1,"cherry")
# list3.append("grapes")
# print(list3)


#take out the data
# list3.pop(0)
# list3.remove("apple")
# print(list3)


#count
res = list3.count("apple")
# print(res)

#extend and sort
list4 = (True,False)

list3.extend(list4)
# print(list4)
# print(list3)

# my_list = [1,2,3,"apple","mango","banana"]
# print("Before sorting:- ",my_list)
# my_list.sort()
# print("After sorting:- ",my_list)
'''

Method	        Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()   	Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

'''
'''
Tuple :- ()
unchangeable
ordered
allows duplication
capable to hold multiple data type

'''

tuple1 = (1,2,3,"C++")

# tuple2 = (5,10,True)
# tuple1 = tuple1+tuple2
# print(tuple1)

# # set and frozenset

set1 = {"India","USA"}
# set1 = frozenset(set1)
set1.add("UK")
# set1.remove()
# print(set1)

# lst = ["mumbai","pune"]
# lst[0] = "delhi"
# print(lst)
# typecasting

# lst = [10,20,30]
# print(lst)
# print(type(lst))
# lst = tuple(lst)
# print(lst)
# print(type(lst))

'''
Immutable/Mutable?-

If immutable objects are objects whose value can't change once created, 
a mutable object is an object whose value can change once created.

'''

'''
Set :- {}
dict :- {}
list>tuple>dict>set:  BODMAS
'''
# set1 = {1,2,3,4,5}
# set2 = {1,2,7,8,9}
# result = set1.union(set2)
# result2 = set1.intersection(set2)
# print(result2)

'''
3.7
dict:-mutable
dont allows duplication 
ordered 
index 0,1,2
'''
dict1 = {
    "clg1":[10,12,13],
    "new" : (123,321),
    "clg2":{
        "name":"Sam",
        "age" : 23
    }

}
print(dict1["clg2"]["age"])
