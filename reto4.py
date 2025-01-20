def minimo_numero_no_formable():
    n=int(input("cuantas monedas?: "))
    

    monedas=[]
    for moneda in range(n):
        valorMoneda=int(input(f"Que valor tiene la moneda? {moneda+1}:  "))
        monedas.append(valorMoneda)
    
    monedas.sort()
    cambio_actual=0

    for i in monedas:
        if i> cambio_actual+1:
            return cambio_actual+1
    
        cambio_actual= cambio_actual+i

    return cambio_actual+1


print("valor minimo que NO se puede formar", minimo_numero_no_formable())
