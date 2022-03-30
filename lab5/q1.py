# a

def add(x, y):
      return x+y

def subtract(x, y):
      return x-y

def multiply(x, y):
      return x*y

def divide(x, y):
      return x/y

x = int(input("Enter x: "))
y = int(input("Enter y: "))
op = input("Enter op: ")[0]
if op=='+':
      r = add(x, y)
elif op=='-':
      r = subtract(x, y)
elif op=='*':
      r = multiply(x, y)
elif op=='/':
      r = divide(x, y)
print(x, op, y, "=", r)

# c

print("Q1C")

A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]   
B = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]] 
result = []
for row_a, row_b in zip(A, B):
      row_r = []
      for item_a, item_b in zip(row_a, row_b):
            row_r.append(item_a*item_b)
      result.append(row_r)
_ = [print(r) for r in result]

# F

def Fibonacci(n):
      if n < 0:
            print("Incorrect input")
      elif n == 0:
            return 0
      elif n == 1 or n == 2:
            return 1
      else:
            return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))

# H

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print( A | B )
print( A & B )
print( A - B )
print( A ^ B )

# I

flag = True
list1 = [int(i) for i in input("Enter nos: ").split()]
for index in range(len(list1)//2):
      if (list1[index]!=list1[len(list1)-index]):
            flag = False
if flag:
      print("Palindrome")
else:
      print("Not a Palindrome")

# J