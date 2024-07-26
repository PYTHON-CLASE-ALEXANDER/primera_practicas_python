                    #MOSTRAR POR PANTALLA
#1. Imprime las siguientes variables x=10; y=20; z=35 en un
#solo comando. El resultado deberia ser: 10 20 35
x=10
y=20
z=35
print(x, y, z)

#2. Ahora modifica el comando anterior para que el resultado se muestre separado por comas 10, 20, 35.
x="10"
y="20"
z="35"
print(x + ", " + y + ", " + z)
print(x,y,z, sep=', ')
print(f"{x}, {y}, {z}.")