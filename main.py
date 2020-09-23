import modules.controlers.meshes as malha
import modules.plots.plot as plt

def main():
    
    # Malha Original
    malhaOriginal = malha.Original()
    malhaOriginal.execute()

    # Malha Aberta
    malhaAberta = malha.Aberta() # Instanciando classe
    malhaAberta.execute() # Executando as operações baseadas nas esquações a diferenças

    # # Malha Fechada 
    malhaFechada = malha.Fechada()  # Instanciando classe
    malhaFechada.execute() # Executando as operações baseadas nas esquações a diferenças

    # Malha Fechada com ganho
    FechadaComGanho = malha.FechadaComGanho()  # Instanciando classe
    FechadaComGanho.execute() # Executando as operações baseadas nas esquações a diferenças

    # Malha Fechada com ganho proporcional e integral
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças

    # Malha Fechada com ganho proporcional, integral e derivativo
    FechadaComGanhoIntegralDerivativo = malha.FechadaComGanhoIntegralDerivativo()
    FechadaComGanhoIntegralDerivativo.execute()

    # plt.plotMalha(malhaAberta)
    plt.plotMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral, FechadaComGanhoIntegralDerivativo])
    # plt.saveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral, FechadaComGanhoIntegralDerivativo])
    # plt.plotAndSaveMalha(FechadaComGanhoIntegral)
    # plt.plotAndSaveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral, FechadaComGanhoIntegralDerivativo])

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
