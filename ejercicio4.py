                                #BUCLES
#1. Escribe el codigo para bucle tipo for el cual imprimie del numero 0 hasta el 7. 
#Utiliza una variable auxiliar llamada n
# for n in range(8):
#     print(n)

#3. Ahora modifica el bucle para que escriba en 3 segundos 99 numeros. piensa con cuidado los 
#valores iniciales y finales del rango
# for n in range(3 , 99, 3): #El primer 3 es con el primer numero que se va a iniciar, el 99 el numero en donde termina y el otro numero 3 es para que se cuente de 3 en 3
#     print(n)

#4. Programa un bucle que haga una cuenta atras de 10 hasta 1 y por ultimo escriba el mensaje 
#'¡Despegue!':
# for n in range(10 , 0, -1):
#     print(n)
# print("¡Despegue!")

#5. Mediante un bucle, escribe el codigo de la tortuga para que
#dibuje un cuadrado (elige tú las dimensiones)
# from turtle import *
# for n in range(4):
#     forward(100)
#     right(90)

#circulo lento
# from turtle import *
# for n in range(360):
#     forward(1)
#     right(1)

#circulo rapido
# from turtle import *
# for n in range(360):
#     circle(100)

#Triangulo
from turtle import *
for n in range(3):
    forward(200)
    right(-120)
