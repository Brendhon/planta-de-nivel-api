import json
import scipy.io as sio

def readJson():
    
    # Lendo o arquivo JSON
    with open('data.json') as json_data:
        constants = json.load(json_data)
        json_data.close()
    
    return constants

def readMat():
    
    # Carregando o arquivo mat
    x = sio.loadmat('modules/data/variables/amostras_equipe2.mat')
    return x['degrau0_2'], x['resp0_2'], x['tempo0_2']