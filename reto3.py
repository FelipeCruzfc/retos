def minimo_numero_no_formable(monedas):
    monedas.sort()
    cambio_actual=0

    
    for i in monedas:
        if i> cambio_actual+1:
            return cambio_actual+1
        cambio_actual+=i



    return cambio_actual+1
        

        
        
print(minimo_numero_no_formable([5,7,1,1,2,3,22]))
print(minimo_numero_no_formable([1,1,1,1,1]))


