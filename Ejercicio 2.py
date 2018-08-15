# Definir una función que calcule el salario neto
def salario_neto(salario,tasa):
    '''
    Calcula el salario neto descontando la retencion en la fuente

    >>> salario_neto(100,2)
    98.0

    >>> salario_neto(200,10)
    180.0
    >>> salario_neto(100,0)
    100.0

    :param salario: (num) El salario del empleado
    :param tasa: (num) La tasa de retefuente (entre 0 y 100)
    :return: (num) El salario neto del empleado
    '''

    sal_neto = salario * (100 - tasa) / 100
    return sal_neto

#Llamar la función 3 veces

salario_neto1 = salario_neto(float(input('Digite su salario')), float(input('digite su tasa')))
salario_neto2 = salario_neto(float(input('Digite su salario')), float(input('digite su tasa')))
salario_neto3 = salario_neto(float(input('Digite su salario')), float(input('digite su tasa')))

#Calcule el salario neto total
print(salario_neto1+salario_neto2+salario_neto3)

