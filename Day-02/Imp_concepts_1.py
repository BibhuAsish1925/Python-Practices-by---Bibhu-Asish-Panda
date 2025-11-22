a = 10
b = "bibhu"
c = 5
d = "roshni"
e = 2.1
f = True
g = complex(8,2)
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
dict1 = {"name":"bibhu", "age":19, "canVote":True}

print(a+c)                                  #output = 15
print(b + d)                                #output = bibhuroshni
print(g)                                    #output = (8+2j)
print(a+e)                                  #output = 12.1 (possible)
print(a+g)                                  #output = (18+2j) (possible)
print(list1)                                #output = [8, 2.3, [-4, 5], ['apple', 'banana']]
print(tuple1)                               #output = (('parrot', 'sparrow'), ('Lion', 'Tiger'))
print(dict1)                                #output = {'name': 'bibhu', 'age': 19, 'canVote': True}


print(type(a))                              #output = <class 'int'>
print(type(b))                              #output = <class 'str'>
print(type(e))                              #output = <class 'float'>
print(type(f))                              #output = <class 'bool'>
print(type(g))                              #output = <class 'complex'>
print(type(a),type(b),type(e),type(f))      #output = <class 'int'> <class 'str'> <class 'float'> <class 'bool'>
print(type(list1))                          #output = <class 'list'>
print(type(tuple1))                         #output = <class 'tuple'>
print(type(dict1))                          #output = <class 'dict'>

#invalids
#print(type(a,b))           #syntax error
#print(a+b)                 #it shows error since both a and b are of different types
#print(list1+a)             #it shows error since both a and list1 are of different types
#print(list1+tuple1)        #it shows error since both tuple1 and list1 are of different types


