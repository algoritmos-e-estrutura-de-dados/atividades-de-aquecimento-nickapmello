a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
maior = 0
while (maior < a or maior < b or maior < c):
    if maior <a:
        maior = a
    elif maior < b:
        maior = b
    else:
        maior = c

print(format(maior)+ " eh o maior")