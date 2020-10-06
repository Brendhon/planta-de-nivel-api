import numpy as np

numeroCasas = 2

def errorCalculate(sp, finalValue):
	return abs(round(sp - finalValue, 2))

def temOvershoot(array, pv):
	valorPossivel1 = round(pv*0.98, numeroCasas)
	valorPossivel2 = round(pv/0.98, numeroCasas)

	for value in array:
		if(value > valorPossivel2 or value < valorPossivel1):
			return True

	return False

def accommodationPoint(array, pv):	

	# Variaveis auxiliares	
	melhorValor = 0

	valorPossivel1 = round(pv*0.98, numeroCasas)	
	valorPossivel2 = round(pv/0.98, numeroCasas)

	for i in range(len(array)):	
		newArray = array[i:]
		if(array[i] >= valorPossivel1 and array[i] <= valorPossivel2 and temOvershoot(newArray, pv) == False):
			melhorValor = array[i]
			break
		
	return melhorValor

def calculateCsi(mp):
	aux = (np.log(mp)/np.pi)**2
	csi = np.sqrt(aux/(1+aux))
	return csi

def calculateWn(csi, ts):
	wn = 4/(csi*ts)
	return wn

def calculateWcg(wn):
	return wn

def calculateMF(csi):
	mf = 2*np.arcsin(csi)*(180/np.pi)
	return mf

def calculateG(k, tal, wcg):
	np.imag = (tal*wcg)*1j
	g = k/(np.imag+1)
	return g

def calculateModG(g):
	modG = abs(g)
	return modG

def calculateFaseG(g):
	faseG = np.angle(g)*180/np.pi
	return faseG

def calculateModC(modG):
	modC = 1/modG
	return modC

def calcualteFaseC(mf, faseG):
	faseC = -180 + mf - faseG
	return faseC

def calculateKp(modC, faseC):
	faseC = (faseC*np.pi)/180
	tan = np.tan(faseC)
	kp = np.sqrt((modC**2)/(1+((tan*(-1))**2)))
	return kp

def calcualteKi(faseC, wcg, kp):
	faseC = (faseC*np.pi)/180
	tan = np.tan(faseC)
	ki = (tan)*(-1)*wcg*kp
	return ki

def calculateKpKi(mp, ts, k, tal):
	csi = calculateCsi(mp)
	wn = calculateWn(csi, ts)
	wcg = calculateWcg(wn)
	mf = calculateMF(csi)
	g = calculateG(k, tal, wcg)
	modG = calculateModG(g)
	faseG = calculateFaseG(g)
	modC = calculateModC(modG)
	faseC = calcualteFaseC(mf, faseG)
	kp = calculateKp(modC, faseC)
	ki = calcualteKi(faseC, wcg, kp)

	return kp, ki
	
if __name__ == "__main__":
	mp = 0.10
	ts = 70
	k = 0.8447
	tal = 280

	kp, ki = calculateKpKi(mp, ts, k, tal)

	print(kp)
	print(ki)