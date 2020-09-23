from matplotlib import pyplot

def saveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Plotanto o ponto de acomodação
    if malha.tempo_acomodacao != 0:
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
        if malha.tempo_acomodacao != 0:
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
    if malha.tempo_acomodacao != 0:
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
        if malha.tempo_acomodacao != 0:
            pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
            pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.show()

def plotAndSaveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}')
    pyplot.legend()

    # Plotanto o ponto de acomodação
    if malha.tempo_acomodacao != 0:
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
        pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Mostrando os dados e a grade
    text = f'{malha.overshoot}\nValor de acomodação: {malha.valor_acomodacao}\nTempo de acomodação: {malha.tempo_acomodacao}s'
    pyplot.text(0.5, 0.3, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})
    pyplot.grid(True)

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.savefig(f'img/{malha.legenda}.png')
    pyplot.show()

def plotAndSaveMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:
        pyplot.plot(malha.resposta, label=f'{malha.legenda}')
        pyplot.legend()

        # Plotanto o ponto de acomodação
        if malha.tempo_acomodacao != 0:
            pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao)
            pyplot.annotate(f'x = {malha.tempo_acomodacao}\ny = {malha.valor_acomodacao}', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/malhas.png')
    pyplot.show()