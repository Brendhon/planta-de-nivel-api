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

    # Malha Fechada com ganho
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças

    # Malha Fechada com ganho
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Instanciando classe
    FechadaComGanhoIntegral.execute() # Executando as operações baseadas nas esquações a diferenças

    plt.plotMalha(FechadaComGanhoIntegral)
    # plt.plotMalhas([malhaOriginal, malhaAberta])
    # plt.saveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral])
    # plt.plotAndSaveMalha(FechadaComGanhoIntegral)
    # plt.plotAndSaveMalhas([malhaAberta, malhaFechada, FechadaComGanho, FechadaComGanhoIntegral])

if __name__ == '__main__': # chamada da funcao principal
    main() # chamada da função main
