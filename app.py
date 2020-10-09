from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import modules.controlers.meshes as malha
import modules.data.constants as const
import json

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        # Pegando os dados da Requisição 
        data = request.get_json()

        try:
            const.SP = data['sp']
        except:
            pass
            
        try:
            const.OVERSHOOT = data['overshoot']
        except:
            pass
        
        try:
            const.TS = data['ts'] 
        except:
            pass

        # Executando as operações
        malhaOriginal.execute()
        malhaOriginalEmRespostaEntrada.execute()
        malhaAberta.execute()
        malhaFechada.execute()
        FechadaComGanho.execute()
        FechadaComGanhoIntegral.execute()

        return jsonify(data), 201
    else:

        # Formando o objeto que será enviado em formato JSON
        malhas = {
            f'{malhaOriginal.nome}': malhaOriginal.returnData(), 
            f'{malhaOriginalEmRespostaEntrada.nome}': malhaOriginalEmRespostaEntrada.returnData(), 
            f'{malhaAberta.nome}': malhaAberta.returnData(), 
            f'{malhaFechada.nome}': malhaFechada.returnData(),
            f'{FechadaComGanho.nome}': FechadaComGanho.returnData(), 
            f'{FechadaComGanhoIntegral.nome}': FechadaComGanhoIntegral.returnData()
        }

        print(FechadaComGanhoIntegral.overshoot)

        return jsonify(malhas)

if __name__ == '__main__':

    # Instanciando classes
    malhaOriginal = malha.Original() # Malha Original
    malhaOriginalEmRespostaEntrada = malha.OriginalEmRespostaEntrada() # Malha minimos quadrados 
    malhaAberta = malha.Aberta() # Malha Aberta
    malhaFechada = malha.Fechada()  # Malha Fechada 
    FechadaComGanho = malha.FechadaComGanho()  # Malha Fechada com ganho
    FechadaComGanhoIntegral = malha.FechadaComGanhoIntegral()  # Malha Fechada com ganho proporcional e integral

    app.run(debug=True)