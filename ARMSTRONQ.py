import math

n = int(input(": "))
a=str(n)
c=[]
for i in range(len(a)):
    b= int(a[i])**3
    c.append(b)
    toplam = sum(c)
print(toplam)

if toplam == n:
    print("Bu armstronq reqemdir")
else:
    print("Bu armstronq reqem deyil")
    