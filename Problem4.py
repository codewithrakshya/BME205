#BME205 Fall23
#Rakshya Sharma
def sum(a, b):
    sum =0
    for i in range(a, b+1):
        if (i % 2!= 0):
            sum = sum +i
    return sum
a = int(input())
b = int(input())
print(sum(a,b))

