lst = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# even = [ all the even no]
# odd = [ all the odd no]

even = [i for i in lst if i%2==0]
odd = [i for i in lst if i%2 != 0]

# lst = [expression for i in expression if condition == True]
# for i in lst:
#     if i%2 ==0:
#         even.append(i)
#     else:
#         odd.append(i)


print(even)
print(odd)


# justify

tuple1 =(11,)
print(type(tuple1))

'''
basics
if else while
fun rec
oops
inheritance

lots of practice
edabit/hackerank....!

stack queue linkedlist
binary b tree b+tree
graphs
bfs dfs
sorting


DBMS

1) very basic
2)basic
3)medium
4)hard

5)very hard
.....
.
.
.
wrong ans


stcak :
push pop algo + code
overflow underflow
application :-  solving infix operation using stack


queue:
enqueue dequeue algo + code


linked list

'''
def is_palindrome(word):
    length = len(word)
    if (length>1):
        if (word[0]==word[length-1]):
            word=word[1:length-1]
            is_palindrome(word)
        else:
            return
        return False
    else:
        return True
    #Remove pass and write your logic here

#Provide different values for word and test your program
result=is_palindrome("MadaM")
if (result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")

# qudractic equ ax**2+bx+c     lib  root = (-b +- (b**2 -4ac)**0.5)/2a

'''
Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste(fname):

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"



Create a method in the Person class which returns how another person's age compares. 
Given the objects p1, p2 and p3, which will be initialised with the attributes name and age,
 return a sentence in the following format:

{other_person} is {older than / younger than / the same age as} me.

Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)
p1.compare_age(p2) ➞ "Joel is older than me."

p2.compare_age(p1) ➞ "Samuel is younger than me."

p1.compare_age(p3) ➞ "Lily is the same age as me."
'''

class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    
    def commpare_age(self,obj):
        if self.age>obj.age:
            print(f"{obj.name} is younger than me")
        elif self.age<obj.age:
            print(f"{obj.name} is older than me")
        else:
            print(f"{obj.name} is same age as me")



p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
p3 = Person("Lily", 24)


# class Person:
    
#     def __init__(self, name, food_like, food_hate):
#          self.name=name
#          self.like_lst=food_like
#          self.hate_lst=food_hate
    
#     def taste(self,food_name):
#          if food_name in self.like_lst:
#              print(f"{self.name} eats {food_name} and loves it")
#          elif food_name in self.hate_lst:
#             print(f"{self.name}eats {food_name} and hates it")
#          else:
#             print(f"{self.name}eats {food_name} !")

        
# p1=Person("Sam","icecream","carrot")
# p1.taste("icecream")

# class Person:

#     def __init__(self, name, likes, hates):
#         self.name = name
#         self.likes = likes
#         self.hates = hates

#     def tastes(self, l):
       
#             if l in self.likes:
#                 print(self.name, "eats", l, "loves it!")
#             elif l in self.hates:
#                 print(self.name, "eats", l, "hates it!")
#             else:
#                 print(self.name, "eats", l + "!")


# p1 = Person("Sam",["ice cream", "carrots", "cheese", "ice cream"], ["carrots"])
# p1.tastes("cheese")

# class Person:
#     def __init__(self, name, like_lst, hate_lst):
#         self.name = name
#         self.like_lst = like_lst
#         self.hate_lst = hate_lst
    
#     def taste(self, fname):
#         if fname in self.like_lst:
#             print(f"{self.name} eats the {fname} and loves it!")
#         elif fname in self.hate_lst:
#             print(f"{self.name} eats the {fname} and hates it!")
#         else:
#             print(f"{self.name} eats the {fname}!")

# p1 = Person("Sam", ["ice cream"], ["carrots"])
# p1.taste("ice cream")
