def preparar_datos(info):
 # Supone que 'info' será un conjunto, pero realmente espera una lista
 acumulador = ""
 for (letra) in (info):
   #Segun el ciclo for, se coloca el nombre de las variables dentro de parentesis
  acumulador += letra + "-"
 return acumulador[:-1]
def mezcla_datos(a, b):
 # Compara dos cosas que no se deberían comparar directamente
 if a > b:
  return a + b
 elif a == b:
  return a * 2
 else:
  return b + a
def iniciar():
 variable1 = input("Ingresa un valor de referencia textual: ")
 variable2 = input("Ingresa otra unidad: ")
 #Solo sustitui el termino de "valor 1" por "variable 1"
 x = preparar_datos(variable1)#Defini el termino de "variable1" como una variable x y "preparar_datos" es para indicar que se va a iniciar un analisis
 y = preparar_datos(variable2) #aqui hice lo mismo pero con el termino de "variable 2"
 resultado = mezcla_datos(x, y)
 print("Resultado no final: ", resultado)
 # El siguiente bloque debe imprimir solo si 'variable1' está en 'variable2'. Se refiere a que si el primer valor es igual al segndo hara lo siguiente
 if variable1 == variable2:
     #atuve que poner dos signos'=' en vez del "in"
  print("Coincidencia detectada") # Error intencional de indentación
  #Necesitaba un espacio para solucionar el error de indentacion
iniciar()