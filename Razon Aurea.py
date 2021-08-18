# " " " Este codigo calcula e imprime " " " 

# " " " la razon aurea " " " 

# " " "  Parametros de entredad: " " " 
# " " "  N = el numero de veces que se va repetir el codigo " " " 
# " " "  para que la razon aurea sea mas exacta " " " 

# " " "  Autor: Maria Camila Vargas  " " " 
# " " "  ULTIMA ACTUALIZACION: 18 de agosto / 2021 " " " 


n  = int(input("Ingrese valor n: ")) # Variable n que guarda la cantidad de iteraciones fibonacci a calcular, es ingresado por el usuario

previo1 = 1 # Almacena el valor de Fibonacci n-1 
previo2 = 1 # Almacena el valor de Fibonacci n-2

if n >= 2: # n es mayor igual a 2
    for i in range(2,n+1): #Ciclo que va desde 2 hasta n
        temp = previo1 # Variable temporal que guarda el valor que hay en previo1, evitando que se pierda
        previo1 = previo1 + previo2 # Modifica el valor de previo1 con el valor de Fibonacci calculado en la iteración
        previo2 = temp # Actualiza el valor de previo2 con el valor almacenado en temp
aurea = 1.618033988749894848204586834365638 # variable que contiene el número aureo
cociFibo = previo1/previo2 #Cociente de la sucesión fibonacci
print("Número aurea:",1.618033988749894848204586834365638) #Imprime el valor de numero aureo para compararlo con el cociente de la sucesión fibonacci
print("fibo(n+1)/fibo(n): ",previo1/previo2) #Imprime el cociente de la sucesión fibonacci(F n+1/F n)
