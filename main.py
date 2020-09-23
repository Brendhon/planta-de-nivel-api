import modules.controlers.meshes as malha
import modules.plots.plot as plt

def main():
    
    # Malha Original
    # malhaOriginal = malha.Original()
    # malhaOriginal.execute()

    # Malha Aberta
    malhaAberta = malha.Aberta() # Instanciando classe
    malhaAberta.execute() # Executando as operações baseadas nas esquações a diferenças

    # # Malha Fechada 
    # malhaFechada = malha.Fechada()  # Instanciando classe
    # malhaFechada.execute() # Executando as operações baseadas nas esquações a diferenças

    # # Malha Fechada com ganho
    # FechadaComGanho = malha.FechadaComGanho()  # Instanciando classe
    # FechadaComGanho.execute() # Executando as operações baseadas nas esquações a diferenças

    # # Malha Fechada com ganho
    # FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    # FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças

    # Malha Fechada com ganho
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças

    # # Malha Fechada com Ganho proporcional, integral e derivativo 
    # malhaComGanhoIntegralDerivativo = malha.FechadaComGanhoIntegralDerivativo() # Instanciando classe
    # malhaComGanhoIntegralDerivativo.execute() # Executando as operações baseadas nas esquações a diferenças

    # plt.saveMalha(malhaAberta)
    plt.plotMalha(FechadaComGanhoIntegral)
    # plt.saveMalhas([malhaAberta,FechadaComGanhoIntegral])

    # plt.plotMalhas([malhaAberta,FechadaComGanhoIntegral])

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
