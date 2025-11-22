"""different loop method"""


"""for loop"""
print("for loop")

for i in range(5):
    print("Hello")

print()

a=5
b=10
c=a+b
for i in range(1, 6):
    print("Hello", i)
    print(c)
print(a,b)
print("bibhu")

print()
print()


"""while loops"""
print("while loops")
count = 0
while count <= 5:
    print(count)
    count += 1

print()

count = 0
while count < 5:
    print(count)
    count += 1

print()

count = 0
while count < 5:
    print(count)
    count += 2

print()
print()


"""list comprehension loop"""
print("list comprehension loop")
nums = [i for i in range(5)]
print(nums)

print()
print()


"""Loop using map()"""
print("Loop using map()")

def show(x):
    print(x)
list(map(show, range(5)))

print()
print()


"""Loop using recursion (function calling itself)"""
print("Loop using recursion (function calling itself)")
def loop(n):
    if n == 0:
        return
    print("Hello")
    loop(n-1)
loop(5)

print()
print()


"""Loop using iterators"""
print("Loop using iterators")
nums = iter([1, 2, 3])
print(next(nums))
print(next(nums))
print(next(nums))

print()
print("end")
print()