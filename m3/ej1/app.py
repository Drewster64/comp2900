def calcular_promedio(num1, num2):
    return (num1 + num2) / 2
#test
promedio_calculado = calcular_promedio(4, 6)
assert promedio_calculado != 5, "El promedio calculado es correcto."