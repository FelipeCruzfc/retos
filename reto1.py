

n = int(input("¿Cuántos números quieres ingresar? "))

Lista_1 = []  
for i in range(n):
    numero=int(input(f"ingrese el numero {i+1}:  "))
    Lista_1.append(numero)
S = 6
nueva_lista = []


for numero in Lista_1:
   
    numero_str = str(numero)

    nuevo_numero=""

    for digito in numero_str:
        if int(digito) <S:
            nuevo_numero+=digito
    
    if nuevo_numero:
        nueva_lista.append(int(nuevo_numero))


nueva_lista=nueva_lista[::-1]

print(nueva_lista)