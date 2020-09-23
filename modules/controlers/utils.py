def calculateOvershoot(array, sp):

    # Variaveis auxiliares
    overshoot = 0.0
    maiorValor = 0

    maiorValor = max(array, key=float)

    if sp < maiorValor:
        overshoot = round((maiorValor - sp)/sp * 100, 2)
    
    return overshoot