
Crie um programa que mostre a quantidade de dígitos que a soma de dois números 
inteiros possui 

a = int(input("a: "))
b = int(input("b: "))
c = a + b
div = 2
n = 0
c = c // div
n += div

print(f"número de dígitos = {n}")

#n += 1
#c = c % div
#print(f"soma = {c}")
#div = 10
#c = a + b
#while c:
