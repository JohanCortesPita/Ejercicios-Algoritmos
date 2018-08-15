#Definir una función que calcule el dolar a peso
def dolar_a_peso(dolar,peso):
    '''
    (float,float) = float
    Calcule la conversion de dolar a peso

    >>> dolar_a_peso(5,3000)
    15000
    >>> dolar_a_peso(2,3000)
    6000

    :param dolar: Cantidad de dolares
    :param peso: Valor de peso
    :return: Valor total de pesos
    '''

    return dolar * peso


