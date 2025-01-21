def numero_cuadrado():
   S=6
   limite= S*S
   arr=[]

   n=int(input("Cuantos numeros va a ingresar?  "))
   for i in range(n):
      numero=int(input(f"Ingrese el numero {i+1}: "))
      arr.append(numero)

   lista_numeros_cuadrados =[]
   for numero in arr:
      cuadrados = numero*numero
      if cuadrados <=limite:
         lista_numeros_cuadrados.append(cuadrados)

  

   resultado_lista =[]
   for num in lista_numeros_cuadrados:
      inserted=False
      for i in range(len(resultado_lista)):
         if num < resultado_lista[i]:
            resultado_lista.insert(i,num)
            inserted=True
            break
         
      if not inserted:
         resultado_lista.append(num)


   return resultado_lista
   



print(numero_cuadrado())