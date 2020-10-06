import modules.data.constants as const
from abc import ABC, abstractmethod
import control as con
from modules.controlers.utils import accommodationPoint, errorCalculate
from numpy import arange
from matplotlib import pyplot

class Malha(ABC):

    def __init__(self, legend, color):

        self.ts = const.TEMPO_AMOSTRAGEM
        self.sys = con.TransferFunction(const.COEFICIENTE_B1,  [1, -const.COEFICIENTE_A1], self.ts)

        self.SP = const.SP
        self.kp = const.KP
        self.ki = const.KI

        self.tempo = const.TEMPO_CALCULO

        self.xout = []
        self.yout = []
        self.valorEstacionario = 0

        self.legenda = legend
        self.cor = color

        self.overshoot = 0
        self.overshootX = 0	
        self.overshootY = 0

        self.tempo_acomodacao = 0	
        self.valor_acomodacao = 0

        self.erroRegimePermanente = 0
        
    @abstractmethod
    def execute(self):
        pass

class Original(Malha):

    def __init__(self):
        super().__init__('Malha Original', 'lime')
    
    def execute(self):
        self.xout =  const.TEMPO[0]
        self.yout = const.SAIDA[0]
        self.valorEstacionario = self.yout[len(self.yout)-1]
        

class OriginalEmRespostaEntrada(Malha):

    def __init__(self):
        super().__init__('Malha Original em Resposta a entrada', 'y')
        self.SP = const.ENTRADA[0][1]
    
    def execute(self):

        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(self.sys, const.TEMPO)

        # Pegando as informações do sistema
        info = con.step_info(self.sys, self.xout)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.SP

        # Pegando o valor de estado estacionário  
        self.valorEstacionario = info['SteadyStateValue']*self.SP

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak']*self.SP
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.SP,self.valorEstacionario)

class Aberta(Malha):

    def __init__(self):
        super().__init__('Malha Aberta', 'dimgray')

    def execute(self):

        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(self.sys, self.tempo)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.SP

        # Pegando as informações sobre o sistema 
        info = con.step_info(self.sys, self.xout)
        
        # Pegando o valor de estado estacionário  
        self.valorEstacionario = info['SteadyStateValue']*self.SP

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak']*self.SP
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.SP,self.valorEstacionario)
             
class Fechada(Malha):

    def __init__(self):
        super().__init__('Malha Fechada', 'orange')
    
    def execute(self):

        # Realimentando a malha
        sysFechada = con.feedback(self.sys, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, self.tempo)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.SP

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)
        
        # Pegando o valor de estado estacionário  
        self.valorEstacionario = info['SteadyStateValue']*self.SP

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak']*self.SP
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.SP,self.valorEstacionario)

class FechadaComGanho(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional', 'r')
           
    def execute(self):

        # Atribuindo o ganho
        sysGanho = self.sys*self.kp

        # Realimentando a malha
        sysFechada = con.feedback(sysGanho, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, self.tempo)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.SP

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)
        
        # Pegando o valor de estado estacionário  
        self.valorEstacionario = info['SteadyStateValue']*self.SP

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak']*self.SP
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.SP,self.valorEstacionario)

class FechadaComGanhoIntegral(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional e integral', 'navy')
    
    def execute(self):

        # Criando a função de transferência auxiliar
        sysAux = con.TransferFunction([1, 0],  [1, -1], self.ts)

        # Criando a transferência do controlador
        sysControlador = sysAux*self.ki*self.ts + self.kp
        
        # Realimentando a malha
        sysGanhoIntegral = con.feedback(sysControlador*self.sys, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysGanhoIntegral, self.tempo)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.SP

        # Pegando as informações sobre o sistema
        info = con.step_info(sysGanhoIntegral, self.xout)
        
        # Pegando o valor de estado estacionário  
        self.valorEstacionario = info['SteadyStateValue']*self.SP

        # Ponto de acomodação
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.valorEstacionario)

        # Overshoot
        self.overshootX = info['PeakTime']
        self.overshootY = info['Peak']*self.SP
        self.overshoot = info['Overshoot']

        # Erro em regime permanente
        self.erroRegimePermanente = errorCalculate(self.SP,self.valorEstacionario)