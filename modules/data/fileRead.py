import scipy.io as sio

def readMat():
    
    # Carregando o arquivo mat
    x = sio.loadmat('modules/data/variables/amostras_equipe2.mat')
    return x['degrau0_2'], x['resp0_2'], x['tempo0_2']