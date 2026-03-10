def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12
    
    promedio = (num1 + num2 + num3 + num4) / 4
    print(promedio)
    
    nums = [num1, num2, num3, num4]
    
    maximo = nums[0]
    
    for n in nums:
        if n > maximo:
            maximo = n
            
    print(maximo)
    
    minimo = nums[0]
    for n in nums:
        if n < minimo:
            minimo = n
            
    print(minimo)
    
    rango = maximo - minimo
    print(rango)    
    
