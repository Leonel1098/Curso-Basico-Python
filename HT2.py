
print("Ejercicio 1")
print("Introduzca un número entero positivo")
n=int(input())
for i in range(n): 
    for j in range(i+1):
        print("*",end="")
    print("")
print("---------------------------------------------------------------------------------------------")

print("Ejercicio 2")
print("Introduce un número entero positivo")
n=int(input())
for i in range(n,-1,-1):
      print(i,end=",")
print("")     
print("--------------------------------------------------------------------------------------------")

print("Ejercicio 3")
print("Introduzca un número entero positivo")
n = int(input())
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")