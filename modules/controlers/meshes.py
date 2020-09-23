import modules.data.constants as const
from abc import ABC, abstractmethod
import control as con
from modules.controlers.utils import calculateOvershoot, accommodationPoint

class Malha(ABC):

    def __init__(self, legend):

        self.a1 = const.COEFICIENTE_A1
        self.b1 = const.COEFICIENTE_B1

        self.PV = const.PV
        self.SP = const.SP
        self.tempo = const.TEMPO_AUX
        # self.tempo = const.TEMPO[0]

        self.resposta = []
        self.legenda = legend
        self.overshoot = 0
        self.tempo_acomodacao = 0
        self.valor_acomodacao = 0
    
    @abstractmethod
    def execute(self):
        pass

class Original(Malha):

    def __init__(self):
        super().__init__('Malha Original')
        self.ts = const.TEMPO_AMOSTRAGEM
        self.valorEntrada = const.ENTRADA[0][1]
    
    def execute(self):

        # Função de trasferencia
        sys = con.TransferFunction(self.b1,  [1, -self.a1], self.ts)

        # Resposta ao degrau
        [xout, yout] = con.step_response(sys, const.TEMPO)

        # "Alterando" amplitude do degrau
        self.resposta = yout*self.valorEntrada

        self.overshoot = 'Sem overshoot'

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.resposta[len(self.resposta)-1], self.overshoot)
            
        
class Aberta(Malha):

    def __init__(self):
        super().__init__('Malha Aberta')
    
    def execute(self):
        
        # Malha aberta
        for i in self.tempo:

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*self.SP

        # Calcular overshoot
        self.overshoot = calculateOvershoot(self.resposta, self.SP)

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.PV, self.overshoot)
        
class Fechada(Malha):

    def __init__(self):
        super().__init__('Malha Fechada')
    
    def execute(self):

        # Variavel erro
        erro = 0

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            erro = self.SP - self.PV

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*erro

        # Calcular overshoot
        self.overshoot = calculateOvershoot(self.resposta, self.SP)

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.PV, self.overshoot)


class FechadaComGanho(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional')
        self.kp = const.KP
    
    def execute(self):

        # Variavel erro
        erro = 0

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            erro = self.kp*(self.SP - self.PV)

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*erro

        # Calcular overshoot
        self.overshoot = calculateOvershoot(self.resposta, self.SP)

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.PV, self.overshoot)

class FechadaComGanhoIntegral(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional e integral')
        self.kp = const.KP
        self.ki = const.KI
        self.ts = const.TEMPO_AMOSTRAGEM
    
    def execute(self):

        # Variáveis auxiliares
        erro = 0
        proporcional = 0
        integrador = 0
        controlador = 0

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            erro = self.SP - self.PV

            # Ação Proporcional 
            proporcional = self.kp*erro   

            # Ação Integrador 
            integrador = integrador + self.ki*self.ts*erro

            # Ação controlador 
            controlador = integrador +  proporcional

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*controlador

        # Calcular overshoot
        self.overshoot = calculateOvershoot(self.resposta, self.SP)

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.PV, self.overshoot)


class FechadaComGanhoIntegralDerivativo(Malha):

    def __init__(self):
        super().__init__('Malha Fechada com ganho proporcional, integral e derivativo')
        self.kp = const.KP
        self.ki = const.KI
        self.kd = const.KD
        self.ts = const.TEMPO_AMOSTRAGEM
    
    def execute(self):

        # Variaveis auxiliares
        erro = 0
        proporcional = 0
        integrador = 0
        controlador = 0
        derivador = 0

        # Calculo do erro anterior
        erroAnterior = self.SP - self.PV

        # Malha aberta
        for i in self.tempo:

            # Calculo do erro
            erro = self.SP - self.PV

            # Ação Proporcional 
            proporcional = self.kp*erro   

            # Ação Integrador 
            integrador = integrador + self.ki*self.ts*erro
            
            # Ação Derivador 
            derivador = ((erro - erroAnterior)/self.ts)*self.kd

            # Ação controlador 
            controlador = integrador + proporcional + derivador
            
            # Atualizando erro
            erroAnterior = erro

            # Adicionando PV no array Resposta
            self.resposta.append(self.PV)

            # Calculando um novo valor para o PV
            self.PV = self.a1*self.PV + self.b1*controlador

        # Calcular overshoot
        self.overshoot = calculateOvershoot(self.resposta, self.SP)

        # Calcular ponto de acomodação
        self.tempo_acomodacao, self.valor_acomodacao = accommodationPoint(self.resposta, self.PV, self.overshoot)