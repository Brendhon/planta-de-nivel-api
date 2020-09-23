def calculateOvershoot(array, sp):

    # Variaveis auxiliares
    overshoot = ''
    maiorValor = 0

    maiorValor = max(array, key=float)

    if sp < maiorValor:
        overshoot = f'Overshoot: {round((maiorValor - sp)/sp * 100, 2)}%'
    else:
        overshoot = 'Sem overshoot'
    
    return overshoot

def accommodationPoint(array, pv, overshoot):

    # Variaveis auxiliares
    numeroCasas = 4

    valorPossivel1 = round(pv*0.982, numeroCasas)
    valorPossivel2 = round(pv/0.982, numeroCasas)
    indexP1 = 0
    indexP2 = 0

    # Caso não tenha overshoot
    if overshoot == 'Sem overshoot':

        for i in range(len(array)):
            if round(array[i], numeroCasas) == valorPossivel1:
                indexP1 = i

        return indexP1, valorPossivel1

    # Caso tenha overshoot
    else:
        
        for i in range(len(array)):
            if round(array[i], numeroCasas) == valorPossivel1:
                indexP1 = i
        
        for i in range(len(array)):
            if round(array[i], numeroCasas) == valorPossivel2:
                indexP2 = i
        
        if indexP1 >= indexP2:
            return indexP1, valorPossivel1
        else:
            return indexP2, valorPossivel2
