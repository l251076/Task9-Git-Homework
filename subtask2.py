n = 0
s = 0
m = -1
a = -1
x = int(input("Enter first number: "))
if x != -1:
    m = x
    while x != -1:
        s = s + x
        n = n + 1
        if x < m:
            m = x
        x = int(input("Enter next number: "))
    a = s / n
else: 
    m = -1
    a = -1
print("n =", n)
print("s =", s)
print("m =", m)
print("a =", a)
'# it looks like I learned how to use
git today'

