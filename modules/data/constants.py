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
TEMPO_AUX = arange(0,6,0.1)

# Calculando coeficientes
COEFICIENTE_A1, COEFICIENTE_B1 = calculate()

print(f'COEFICIENTE_A1 = {COEFICIENTE_A1}')
print(f'COEFICIENTE_B1 = {COEFICIENTE_B1}')

# # Valores dos coeficientes da planta de nível
# COEFICIENTE_A1 = 0.99736
# COEFICIENTE_B1 = 0.0019800

# # Valores dos coeficientes de teste
# COEFICIENTE_A1 = 0.904837
# COEFICIENTE_B1 = 0.095163

