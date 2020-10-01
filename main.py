import modules.controlers.meshes as malha
import modules.plots.plot as plt

def main():
    
    # # Malha Original
    malhaOriginal = malha.Original()
    malhaOriginal.execute()

    # Malha Original
    malhaOriginalEmRespostaEntrada = malha.OriginalEmRespostaEntrada()
    malhaOriginalEmRespostaEntrada.execute()

    # Malha Aberta
    # malhaAberta = malha.Aberta() # Instanciando classe
    # malhaAberta.execute() # Executando as operações baseadas nas equações a diferenças

    # # Malha Fechada 
    # malhaFechada = malha.Fechada()  # Instanciando classe
    # malhaFechada.execute() # Executando as operações baseadas nas equações a diferenças

    # Malha Fechada com ganho
    FechadaComGanho = malha.FechadaComGanho()  # Instanciando classe
    FechadaComGanho.execute() # Executando as operações baseadas nas equações a diferenças

    # # Malha Fechada com ganho proporcional e integral
    # FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    # FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas equações a diferenças

    plt.plotMalha(malhaOriginalEmRespostaEntrada)
    # plt.plotMalhas([malhaOriginal, malhaOriginalEmRespostaEntrada])
    # plt.saveMalha(FechadaComGanhoIntegralDerivativo)
    # plt.saveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegralDerivativo])
    # plt.plotAndSaveMalha(malhaAberta)
    # plt.plotAndSaveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral, FechadaComGanhoIntegralDerivativo])

if __name__ == '__main__': # chamada da função principal
    main() # chamada da função main
