from modules.data.fileRead import readJson, readMat
from numpy import arange
from modules.modelar.leastSquares import calculate

# Lendo arquivo JSON
var = readJson()

# Constantes escolhidas
SP = var['SP']
PV = var['PV']
KP = var['KP']
KI = var['KI']
KD = var['KD']

# Pegando vetores de entrada e saída
ENTRADA, SAIDA, TEMPO = readMat()

# Calculando intervalo de tempo
TEMPO_AMOSTRAGEM = TEMPO[0][1]

# Calculando intervalo de tempo
TEMPO_PLOT_INICIO = 0
TEMPO_PLOT_FIM = 40
TEMPO_PLOTAGEM = arange(TEMPO_PLOT_INICIO,TEMPO_PLOT_FIM,TEMPO_AMOSTRAGEM)

# Calculando coeficientes
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

print(f'COEFICIENTE_A1 = {COEFICIENTE_A1}')
print(f'COEFICIENTE_B1 = {COEFICIENTE_B1}')

