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

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Plotanto o ponto de acomodação
    pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
    pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))
    
    # Mostrando os dados e a grade
    text = f'{malha.overshoot}\nValor de acomodação: {malha.valor_acomodacao}\nTempo de acomodação: {malha.tempo_acomodacao}s'
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Salvando a figura
    pyplot.savefig(f'img/{malha.legenda}.png')

def saveMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()    
        # Plotanto o ponto de acomodação
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
        pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Salvando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/malhas.png')

def plotMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Plotanto o ponto de acomodação
    pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
    pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Mostrando os dados e a grade
    text = f'{malha.overshoot}\nValor de acomodação: {malha.valor_acomodacao}\nTempo de acomodação: {malha.tempo_acomodacao}s'
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.show()

def plotMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()
        # Plotanto o ponto de acomodação
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
        pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.show()