t,a,b = input().split(" ")
t,c,d = input().split(" ")
a = float(a)
b = float(b)
c = float(c)
d = float(d)

dinheiro = round((a*b)+(c*d),2)
print("VALOR A PAGAR: R$ "+format(dinheiro))