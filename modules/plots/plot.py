from matplotlib import pyplot

def saveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
    pyplot.legend()

    # Adicionando o ponto de Tempo de acomodação
    pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
    pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Adicionando se tiver o overshoot no gráfico
    if malha.overshootY > malha.PV:
        pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
        pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))		
    
    # Mostrando uma caixa com as informações
    text = f'Valor máximo do overshoot ≅ {round(malha.overshootY, 2)}\nErro em regime permanente ≅ {malha.erroRegimePermanente}\nValor de acomodação ≅ {round(malha.valor_acomodacao, 2)}\nTempo de acomodação ≅ {malha.tempo_acomodacao}s'
    pyplot.text(0.5, malha.resposta[len(malha.resposta) - 1]/2, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})

    # Salvando a figura
    pyplot.grid(True)
    pyplot.savefig(f'img/{malha.legenda}.png')

def saveMalhas(arrayMalha):

# Adicionando todas as malhas no plot
    for malha in arrayMalha:

        # Adicionando ponto de tempo de acomodação no gráfico
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
        pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

        # Adicionando se tiver o overshoot no gráfico
        if malha.overshootY > malha.PV:
            pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
            pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))

        # Adicionando legenda
        pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
        pyplot.legend()

    # Salvando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/Malhas.png')

def plotMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
    pyplot.legend()

    # Adicionando o ponto de Tempo de acomodação
    pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
    pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Adicionando se tiver o overshoot no gráfico
    if malha.overshootY > malha.PV:
        pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
        pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))		
    
    # Mostrando uma caixa com as informações
    text = f'Valor máximo do overshoot ≅ {round(malha.overshootY, 2)}\nErro em regime permanente ≅ {malha.erroRegimePermanente}\nValor de acomodação ≅ {round(malha.valor_acomodacao, 2)}\nTempo de acomodação ≅ {malha.tempo_acomodacao}s'
    pyplot.text(0.5, malha.resposta[len(malha.resposta) - 1]/2, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.show()

def plotMalhas(arrayMalha):

    # Adicionando todas as malhas no plot
    for malha in arrayMalha:

        # Adicionando ponto de tempo de acomodação no gráfico
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
        pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

        # Adicionando se tiver o overshoot no gráfico
        if malha.overshootY > malha.PV:
            pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
            pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))

        # Adicionando legenda
        pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
        pyplot.legend()

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.show()

def plotAndSaveMalha(malha):

    # Plotando a malha e adicionando legenda
    pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
    pyplot.legend()

    # Adicionando o ponto de Tempo de acomodação
    pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
    pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

    # Adicionando se tiver o overshoot no gráfico
    if malha.overshootY > malha.PV:
        pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
        pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))		
    
    # Mostrando uma caixa com as informações
    text = f'Valor máximo do overshoot ≅ {round(malha.overshootY, 2)}\nErro em regime permanente ≅ {malha.erroRegimePermanente}\nValor de acomodação ≅ {round(malha.valor_acomodacao, 2)}\nTempo de acomodação ≅ {malha.tempo_acomodacao}s'
    pyplot.text(0.5, malha.resposta[len(malha.resposta) - 1]/2, text, style='italic',
        bbox={'facecolor': 'cyan', 'alpha': 0.5, 'pad': 10})

    # Mostrando a malha
    pyplot.grid(True)
    pyplot.savefig(f'img/{malha.legenda}.png')
    pyplot.show()

def plotAndSaveMalhas(arrayMalha):

     # Adicionando todas as malhas no plot
    for malha in arrayMalha:

        # Adicionando ponto de tempo de acomodação no gráfico
        pyplot.scatter(malha.tempo_acomodacao,malha.valor_acomodacao, c=malha.cor)	
        pyplot.annotate(f'{malha.tempo_acomodacao}s', (malha.tempo_acomodacao, malha.valor_acomodacao))

        # Adicionando se tiver o overshoot no gráfico
        if malha.overshootY > malha.PV:
            pyplot.scatter(malha.overshootX,malha.overshootY, c=malha.cor)	
            pyplot.annotate(f'{malha.overshoot}%', (malha.overshootX, malha.overshootY))

        # Adicionando legenda
        pyplot.plot(malha.resposta, label=f'{malha.legenda}', color = malha.cor)
        pyplot.legend()

    # Mostrando todas as malhas passadas
    pyplot.grid(True)
    pyplot.savefig('img/Malhas.png')
    pyplot.show()