# Para rodar a API: python api_freq.py
from flask import Flask, request, jsonify
import csv

app = Flask(__name__)


# Função para carregar as frequências de um arquivo CSV
def carregar_frequencias():
    frequencias = {}
    with open('catalogo_animais.csv', mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            animal = row['animal'].strip().lower()
            frequencias[animal] = int(row['frequencia'])
    return frequencias


# Endpoint para obter a frequência de um animal
@app.route('/frequencia/<animal>', methods=['GET'])
def obter_frequencia(animal):
    frequencias = carregar_frequencias()
    freq = frequencias.get(animal.lower(), 0)
    return jsonify({'animal': animal, 'frequencia': freq})


# Endpoint para adicionar um novo animal ao catálogo
@app.route('/adicionar', methods=['POST'])
def adicionar_animal():
    data = request.json
    animal = data['animal'].strip().lower()
    frequencia = data['frequencia']

    with open('catalogo_animais.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([animal, frequencia])

    return jsonify({'message': f"Animal '{animal}' adicionado com sucesso!"})


# Iniciar a API
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
