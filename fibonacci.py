num = int(input("Please give me the number  : "))
a = 0
b = 1
total = 1
for i in range(0, num):
    print(a)
    a,b = b, a + b
list = [b-1]
total = sum(list)
print("Sum: ",total)


