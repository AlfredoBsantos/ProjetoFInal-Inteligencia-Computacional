# Importar as bibliotecas necessárias
from flask import Flask, request, render_template
import joblib
import pandas as pd
import numpy as np

# Inicializar a aplicação Flask
app = Flask(__name__)

# Carregar o modelo de regressão treinado
# Este arquivo .pkl deve estar na mesma pasta que o app.py
try:
    model = joblib.load('housing_regression_model.pkl')
    print("Modelo carregado com sucesso!")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    model = None

# Definir a rota principal da aplicação (a página inicial)
@app.route('/')
def home():
    # Apenas renderiza (mostra) a página HTML principal
    return render_template('index.html')

# Definir a rota para onde os dados do formulário serão enviados para predição
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text='Erro: Modelo não foi carregado.')

    # O bloco try...except começa aqui. Ele tenta executar o código de predição.
    try:
        # Coletar os dados enviados pelo formulário HTML
        features = [
            float(request.form.get('longitude')),
            float(request.form.get('latitude')),
            float(request.form.get('housing_median_age')),
            float(request.form.get('total_rooms')),
            float(request.form.get('total_bedrooms')),
            float(request.form.get('population')),
            float(request.form.get('households')),
            float(request.form.get('median_income')),
            request.form.get('ocean_proximity')
        ]

        # Recalcular as features de engenharia
        if features[6] != 0: # households
            features.append(features[3] / features[6])  # rooms_per_household
            features.append(features[5] / features[6])  # population_per_household
        else:
            features.append(0)
            features.append(0)

        if features[3] != 0: # total_rooms
            features.append(features[4] / features[3])  # bedrooms_per_room
        else:
            features.append(0)

        # Reordenar a lista para a ordem correta das colunas
        # A ordem é: as 9 do form + rooms_per_household + bedrooms_per_room + population_per_household
        # A ordem correta é: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 10]
        final_features = [
            features[0], features[1], features[2], features[3], features[4],
            features[5], features[6], features[7], features[8],
            features[9], # rooms_per_household
            features[11],# bedrooms_per_room
            features[10] # population_per_household
        ]


        # Criar um DataFrame do Pandas com os dados do usuário, na ordem correta
        colunas = [
            'longitude', 'latitude', 'housing_median_age', 'total_rooms',
            'total_bedrooms', 'population', 'households', 'median_income',
            'ocean_proximity', 'rooms_per_household', 'bedrooms_per_room',
            'population_per_household'
        ]
        
        input_data = pd.DataFrame([final_features], columns=colunas)

        # Usar o pipeline carregado para fazer a predição
        prediction = model.predict(input_data)

        # Formatar o resultado para exibição
        output = f'$ {prediction[0]:,.2f}'

        # Renderizar a mesma página, mas agora com o texto da predição
        return render_template('index.html', prediction_text=f'Valor Estimado do Imóvel: {output}')

    # Este é o bloco 'except' que estava faltando ou com a indentação errada.
    # Ele deve estar no mesmo nível de indentação do 'try'.
    except Exception as e:
        # Em caso de erro, mostrar a mensagem de erro na página
        return render_template('index.html', prediction_text=f'Erro ao fazer a predição: {e}')

# Executar a aplicação
if __name__ == "__main__":
    app.run(debug=True)