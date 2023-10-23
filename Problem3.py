#BME205 Fall23
#Rakshya Sharma
def string(s, a, b, c, d):
    return s[a:b+1]+" "+s[c:d+1]
s = input("Enter the String:")
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
print(string(s, a, b, c, d))