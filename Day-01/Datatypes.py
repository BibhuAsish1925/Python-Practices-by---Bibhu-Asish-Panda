#----------------Basics--------------

# int (integer)
a = 10
temp = -5
print("a =", a)
print("temp =", temp)

print()

# float
voltage = 1.98
resistance = 47.5
print("voltage =", voltage)
print("resistance =", resistance)

print()

# str (string)
name = "Bibhu"
msg = "Hello World"
print("name =", name)
print("msg =", msg)

print()

# bool (Boolean)
flag = True
error = False
print("flag =", flag)
print("error =", error)

print()

# list
values = [10, 20, 30]
print("values =", values)

print()

# tuple (Ordered, unchangeable)
coordinates = (10, 20)
print("coordinates =", coordinates)

print()

# set
unique_ids = {1, 2, 3}
print("unique_ids =", unique_ids)

print()

# dict (dictionary)
timing = {
    "path": "U1/U2",
    "slack": -0.23
}
print("timing =", timing)
print("timing['path'] =", timing["path"])
print("timing['slack'] =", timing["slack"])

print()
print()

#----------------Very Important--------------

# Check the Type Using type()
a = 10
print("Type of a:", type(a))

print()

# Type Conversion (Casting)
x = "10"
y = int(x)
print("x (string) =", x)
print("y (converted to int) =", y)

print()

a = 10
b = float(a)
print("a =", a)
print("b (float) =", b)

print()

c = str(100)

print("c (string) =", c)









"""Output - 
a = 10
temp = -5

voltage = 1.98
resistance = 47.5

name = Bibhu
msg = Hello World

flag = True
error = False

values = [10, 20, 30]

coordinates = (10, 20)

unique_ids = {1, 2, 3}

timing = {'path': 'U1/U2', 'slack': -0.23}
timing['path'] = U1/U2
timing['slack'] = -0.23


Type of a: <class 'int'>

x (string) = 10
y (converted to int) = 10

a = 10
b (float) = 10.0

c (string) = 100"""
