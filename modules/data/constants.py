from modules.data.fileRead import readMat
from numpy import arange
from modules.modelar.leastSquares import calculate

# Alternativa para caso as constantes escolhidas não forem escolhidas pelo Usuário
SP = 50
OVERSHOOT = 0.10
TS = 70

# Pegando vetores de entrada e saída
ENTRADA, SAIDA, TEMPO = readMat()

# Calculando intervalo de tempo
TEMPO_AMOSTRAGEM = TEMPO[0][1]

# Calculando intervalo de tempo
TEMPO_CALCULO = arange(0,(len(TEMPO[0])*TEMPO_AMOSTRAGEM),TEMPO_AMOSTRAGEM)

# Calculando coeficientes
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

