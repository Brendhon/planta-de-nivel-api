from matplotlib import pyplot
import control as con
import modules.data.constants as const 

def plotOriginal():

    # Função de trasferencia
    sys = con.TransferFunction(const.COEFICIENTE_B1,  [1, -const.COEFICIENTE_A1], const.TEMPO_AMOSTRAGEM)

    # Resposta ao degrau
    print(sys)
    [xout, yout] = con.step_response(sys, const.TEMPO)

    # "Alterando" amplitude do degrau
    resp = yout*const.ENTRADA[0][1]

    # Plotanto grafico
    name = 'Malha original'
    pyplot.grid(True)

    pyplot.plot(resp, label=name)
    pyplot.legend()
    pyplot.savefig(f'img/{name}.png')
    pyplot.show()

def saveMalha(malha):
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    pyplot.grid(True)
    pyplot.savefig(f'img/{malha.legenda}.png')

def saveMalhas(arrayMalha):

    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()

    pyplot.grid(True)
    pyplot.savefig('img/malhas.png')

def plotMalha(malha):

    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    pyplot.grid(True)
    pyplot.show()

def plotMalhas(arrayMalha):

    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()

    pyplot.grid(True)
    pyplot.show()