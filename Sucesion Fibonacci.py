# " " " Este codigo calcula e imprime " " " 
# " " " los N numeros de la sucesion de fibonacci " " " 

#  " " " Parametros de entredad: " " " 
# " " "  N = cantidad de N numeros de la sucesion a imprimir " " " 

# " " "  Autor: Maria Camila Vargas Giraldo " " " 
# " " "  ULTIMA ACTUALIZACION: 18 de agosto / 2021 " " " 


n  = int(input("Ingrese valor n: ")) # Variable n que guarda la cantidad de números de la sucesión a calcular, es ingresado por el usuario

previo1 = 1 # Almacena el valor de Fibonacci n-1 
previo2 = 1 # Almacena el valor de Fibonacci n-2

if n >= 2: #Si n es mayor igual a 2, entra a calcular la serie
    print(0) # Imprime 0 
    print(1) # Imprime 1
    print(1) # Imprime 2
    for i in range(2,n): #Ciclo que va desde 2 hasta n-1   
        temp = previo1 # Variable temporal que guarda el valor que hay en previo1, evitando que se pierda
        previo1 = previo1 + previo2 # Modifica el valor de previo1 con el valor de Fibonacci calculado en la iteración
        previo2 = temp # Actualiza el valor de previo2 con el valor almacenado en temp
        print(previo1) #Imprime el valor de Fibonacci calculado en la iteración
elif n == 0: #Si n es igual a 0
    print(n) #Imprime el valor de n
elif n==1: #Si n es igual a 1
    print(0) # Imprime 0
    print(1) # Imprime 1
