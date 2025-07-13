# Desenvolvimento e Avaliação de um Modelo de Regressão para Predição de Valores de Imóveis na Califórnia

## 🎯 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina de **Inteligência Computacional** e consiste na criação de uma solução de Machine Learning de ponta a ponta[cite: 4]. O objetivo é desenvolver e avaliar um modelo de regressão capaz de prever o valor mediano de imóveis na Califórnia, com base no dataset `housing.csv`.

O fluxo de trabalho abrange desde a análise e preparação dos dados até a implementação de uma aplicação web funcional para realizar predições em tempo real[cite: 5], cumprindo os seguintes macro-passos:
* **Análise Exploratória e Engenharia de Features:** Para entender as distribuições e criar variáveis mais robustas[cite: 7, 10].
* **Pré-processamento e Modelagem:** Utilizando um pipeline para tratar os dados e comparar múltiplos algoritmos de regressão, como Regressão Linear, Árvore de Decisão e Random Forest [cite: 21][cite_start], além de modelos com regularização L1, L2 e ElasticNet[cite: 24].
* **Otimização e Avaliação:** Uso de Grid Search para otimizar hiperparâmetros e avaliação do melhor modelo no conjunto de teste[cite: 21, 23].
* **Implementação:** Desenvolvimento de uma aplicação web com Flask para consumir o modelo treinado e permitir a interação do usuário final[cite: 25].

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Análise e Modelagem:** Pandas, NumPy, Scikit-learn, Jupyter Notebook
* **Servidor Web (Back-end):** Flask
* **Interface (Front-end):** HTML, CSS

## 📁 Estrutura do Repositório
```

├── Analise_e_Modelo.ipynb
├── app.py
├── housing_regression_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

```

* **`Analise_e_Modelo.ipynb`**: Notebook Jupyter com toda a análise, treinamento e comparação de modelos, que culmina na criação do arquivo `.pkl`.
* **`app.py`**: O script Flask que serve como back-end da aplicação. Ele carrega o modelo e gerencia as predições.
* **`housing_regression_model.pkl`**: O artefato do modelo treinado (pipeline completo), pronto para ser usado em produção.
* **`templates/index.html`**: O arquivo HTML que estrutura o front-end da aplicação.
* **`static/style.css`**: O arquivo CSS que estiliza a interface do usuário.
* **`README.md`**: Este arquivo de documentação.

## 🚀 Como Executar o Projeto

Para executar este projeto, é necessário ter o **Anaconda** ou **Miniconda** instalado.

### 1. Preparação do Ambiente

Abra o **Anaconda Prompt** e siga os passos abaixo para criar um ambiente virtual com todas as dependências.

**a. Crie o ambiente:**
bash
```
conda create --name estatistica python=3.9
```
b. Ative o ambiente recém-criado:

Bash
```
conda activate estatistica
```
c. Instale as bibliotecas necessárias:

Bash
```
conda install notebook flask pandas scikit-learn joblib
```
2. Executando a Aplicação Web
Esta é a forma principal de interagir com o projeto finalizado.

a. Navegue até a pasta raiz do projeto no seu terminal:

Bash
```
cd caminho/para/a/pasta/Inteligencia_Computacional_Projeto
```
b. Execute o servidor Flask:

Bash
```
python app.py
```
c. Acesse a aplicação: Abra seu navegador de internet e acesse o seguinte endereço:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)
Você verá a interface web pronta para receber os dados e fazer predições.

🎬 Apresentação em Vídeo
Uma demonstração completa do projeto, incluindo a navegação pelo notebook e pela aplicação web funcional, está disponível no link abaixo:

Clique aqui para assistir à apresentação no YouTube

✍️ Autores
ALFREDO HENRIQUE SIVEIRA BEZERRA DOS SANTOS
