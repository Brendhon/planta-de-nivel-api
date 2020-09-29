numeroCasas = 2

def calculateOvershoot(array, sp):

	# Variaveis auxiliares
	overshootPorcentagem = 0.0
	overshootX = 0.0
	overshootY = 0.0
	maiorValor = 0

	maiorValor = max(array, key=float)
	overshootPorcentagem = round((maiorValor - sp)/sp * 100, 2)

	for i in range(len(array)):	
		if maiorValor == array[i]: 
			overshootY = array[i]
			overshootX = i

	return overshootX, overshootY, overshootPorcentagem

def temOvershoot(array, pv):
	valorPossivel1 = round(pv*0.98, numeroCasas)
	valorPossivel2 = round(pv/0.98, numeroCasas)

	for value in array:
		if(value > valorPossivel2 or value < valorPossivel1):
			return True

	return False

def accommodationPoint(array, pv, overshoot):	
	# Variaveis auxiliares	
	melhorValor = 1
	melhorIndex = 0

	valorPossivel1 = round(pv*0.98, numeroCasas)	
	valorPossivel2 = round(pv/0.98, numeroCasas)

	for i in range(len(array)):	
		newArray = array[i:]
		if(array[i] >= valorPossivel1 and array[i] <= valorPossivel2 and temOvershoot(newArray, pv) == False):
			melhorIndex = i	
			melhorValor = array[i]
			break
		
	return melhorIndex, melhorValor
