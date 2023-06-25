# Christmas Tree
n = 25
for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()
root = ["||"," __||__"," \    /"," \__/"]
for i in root:
    print( i.center(50, " "))

 # Different patterns 
 # 1.
n= 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
print("\n")

#2.
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()
print("\n")

#3.
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
print("\n")

#4
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print("\n")

#5
row = 5
col = 5
for i in range(row):
    for j in range(col):
        if i == 0 or i == row-1 or j == 0  or j == col - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("\n")

#6
n= 5
for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(n-1):
    for j in range(n - i -1 ):
        print("*", end=" ")
    print()
print("\n")

#7
n= 5
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
for i in range(n-1):
    for j in range(i + 2):
        print(" ", end="")
    for k in range(n - i - 1):
        print("*", end="")
    print()
print("\n")

#8
for i in range(n - 1):
    for k in range(i + 1):
        print(" ", end="")
    for j in range(n - i):
        print("*", end=" ")
    print()
for i in range(n):
    for  j in range(n - i):
        print(" ",end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()
print("\n")

# 9
r = 10
c = 2*r - 1
set = set()
for i in range(r):
    for j in range(c):
        if i > 0:
            set.add(((c - 1)/2))
            set.add(((c - 1)/2)-i + 1)
            set.add(((c - 1)/2)+i - 1)
            object = list(set)
            if j in object:
                print(" ", end="")
            else:
                print("*", end="")
        else:
            print("*", end="")
    print()

   

    
  