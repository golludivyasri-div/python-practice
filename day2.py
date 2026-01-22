#DATATYPES
#INT(whole numbers)
#x=10
#y=-5
#print("x=",type(x))
#print("y=",type(y))
#FLOAT(decimal numbers)
#a=3.4
#print("a=",type(a))
#COMPLEX-numbers with real and imaginary
#z = 2 + 3j
#print("z=",z,type(z)) 
#STRING(sequence of characters)
#name="divyasri"
#print("name:",name)
#print("first letter",name[0])#index
#print("first three letters",name[0:3])#slicing
#print("repeat:",name*3)#repetition
#LIST(mutable sequence:can store multiple items it can be changed)
#list=[1,2,3,"python",5]
#print("list:",list)
#list.append("coding")
#print("after append",list)
#list.remove(2)
#print("after removing",list)
#TOUPLE(immutable sequence:like list but cannot be change)
#touple=("vasu","divya","siddu")
#print("touple",touple)
#print("first name",touple[0])
#DICTIONARY(stores info in key:value format)
#student={"name":"divya sri","college":"IIIT","age":20}
#print("student dict:",student)
#print("name",student["name"])
#student["age"]=21
#print("updated dict",student)
#SET(stores unique items only)
#set={1,2,3,4}
#print("set:",set)
#set.add(5)
#print("updated set",set)
#set.remove(5)
#print("after removed set",set)
#BOOLEAN(true/false)
#a=10
#b=2
#print("is a>b",a>b)
#print("is a<b",a<b)
#NONE
#x= None
#print("x=",type(x))
#EXAMPLES FOR DATA TYPES
#PROGRAM1:(list+sum+bool)
#numbers=[1,2,3,4,5]
#total= sum(numbers )
#print("list:",numbers)
#print("sum:",total)
#print("is sum >10",total>10)
#PROGRAM2:SET+LIST
#num=[1,2,1,3,4,4,5,5,6,4,6]
#uniq=set(num)
#print("orig",num)
#print("uniq",uniq)
#SMALL FUNCTIONS
#1(check even or odd)
#def even(n):
#        return n%2==0
#print("is 7 even?",even(7))
#print("is 10 even?",even(10))
#2(Reverse a string)
#def rev_s(s):
#   return s[::-1]
#print(rev_s("divya"))