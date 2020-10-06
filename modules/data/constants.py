from modules.data.fileRead import readJson, readMat
from numpy import arange
from modules.modelar.leastSquares import calculate

# Lendo arquivo JSON
var = readJson()

# Constantes escolhidas
SP = var['SP']
KP = var['KP']
KI = var['KI']
KD = var['KD']

# Pegando vetores de entrada e saída
ENTRADA, SAIDA, TEMPO = readMat()

# Calculando intervalo de tempo
TEMPO_AMOSTRAGEM = TEMPO[0][1]

# Calculando coeficientes
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

