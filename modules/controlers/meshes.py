import modules.data.constants as const
from abc import ABC, abstractmethod
import control as con
from modules.controlers.utils import calculateOvershoot, accommodationPoint, d2c
from numpy import arange
from matplotlib import pyplot

class Malha(ABC):

    def __init__(self, legend, color):

        self.ts = const.TEMPO_AMOSTRAGEM
        self.sys = con.TransferFunction(const.COEFICIENTE_B1,  [1, -const.COEFICIENTE_A1], self.ts)

        self.PV = const.PV
        self.SP = const.SP
        self.tempo = arange(0,346.8,0.2)

        self.xout = []
        self.yout = []

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
        self.PV = self.yout[len(self.yout)-1]
        

class OriginalEmRespostaEntrada(Malha):

    def __init__(self):
        super().__init__('Malha Original em Resposta a entrada', 'y')
        self.valorEntrada = const.ENTRADA[0][1]
    
    def execute(self):

        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(self.sys, const.TEMPO)

        print(d2c(self.sys, method='zoh'))

        # Pegando as informações do sistema
        info = con.step_info(self.sys, self.xout)

        # "Alterando" amplitude do degrau
        self.yout = self.yout*self.valorEntrada

        self.PV = self.yout[len(self.yout)-1]
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.PV)
        self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        self.erroRegimePermanente = round(self.valorEntrada - self.PV, 2)  

class Aberta(Malha):

    def __init__(self):
        super().__init__('Malha Aberta', 'dimgray')

    def execute(self):

        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(self.sys, self.tempo)

        info = con.step_info(self.sys, self.xout)
        
        self.PV = self.yout[len(self.yout)-1]
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.PV)
        self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        self.erroRegimePermanente = round(self.SP - self.PV, 2)
        
class Fechada(Malha):

    def __init__(self):
        super().__init__('Malha Fechada', 'orange')
    
    def execute(self):

        # Realimentando a malha
        sysFechada = con.feedback(self.sys, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, self.tempo)

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)
        
        self.PV = self.yout[len(self.yout)-1]
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.PV)
        self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        self.erroRegimePermanente = round(self.SP - self.PV, 2)

class FechadaComGanho(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional', 'r')
        self.kp = const.KP
    
    def execute(self):

        # Atribuindo o ganho
        sysGanho = self.sys*self.kp

        # Realimentando a malha
        sysFechada = con.feedback(sysGanho, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, self.tempo)

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)
        
        self.PV = self.yout[len(self.yout)-1]
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.PV)
        self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        self.erroRegimePermanente = round(self.SP - self.PV, 2)


class FechadaComGanhoIntegral(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional e integral', 'navy')
        self.kp = const.KP
        self.ki = const.KI
    
    def execute(self):

        # Atribuindo o ganho
        sysGanho = self.sys*self.kp

        # Realimentando a malha
        sysFechada = con.feedback(sysGanho, 1)
        
        # Resposta ao degrau
        [self.xout, self.yout] = con.step_response(sysFechada, self.tempo)

        # Pegando as informações sobre o sistema
        info = con.step_info(sysFechada, self.xout)
        
        self.PV = self.yout[len(self.yout)-1]
        self.tempo_acomodacao = info['SettlingTime']
        self.valor_acomodacao = accommodationPoint(self.yout, self.PV)
        self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        self.erroRegimePermanente = round(self.SP - self.PV, 2)
        
# class FechadaComGanhoIntegralDerivativo(Malha):

#     def __init__(self):
#         super().__init__('Malha Fechada com ganho proporcional, integral e derivativo', 'teal')
#         self.kp = const.KP
#         self.ki = const.KI
#         self.kd = const.KD
    
#     def execute(self):

#         # Variaveis auxiliares
#         erro = 0
#         proporcional = 0
#         integrador = 0
#         controlador = 0
#         derivador = 0

#         # Calculo do erro anterior
#         erroAnterior = self.SP - self.PV

#         # Malha aberta
#         for i in self.tempo:

#             # Calculo do erro
#             erro = self.SP - self.PV

#             # Ação Proporcional 
#             proporcional = self.kp*erro   

#             # Ação Integrador 
#             integrador = integrador + self.ki*self.ts*erro
            
#             # Ação Derivador 
#             derivador = ((erro - erroAnterior)/self.ts)*self.kd

#             # Ação controlador 
#             controlador = integrador + proporcional + derivador
            
#             # Atualizando erro
#             erroAnterior = erro

#             # Adicionando PV no array Resposta
#             self.yout.append(self.PV)

#             # Calculando um novo valor para o PV
#             self.PV = self.a1*self.PV + self.b1*controlador

#         # Calcular overshoot
#         self.overshootX, self.overshootY, self.overshoot = calculateOvershoot(self.yout, self.SP)
        
#         # Calcular erro em regime permanente
#         self.erroRegimePermanente = abs(round(self.SP - self.PV, 2))

#         self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.yout, self.PV, self.overshoot)

#         self.xout = self.tempo