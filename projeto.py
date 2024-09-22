import requests
import os

# Variável para definir o endereço da API
API_URL = 'http://192.168.0.113:5000'  # Substitua <IP_DO_SERVIDOR> pelo IP real


def disparar_som(animal):
    # Faz uma requisição GET para a API para obter a frequência do animal
    response = requests.get(f'{API_URL}/frequencia/{animal}')
    data = response.json()
    frequencia = data['frequencia']

    if frequencia > 0:
        beep(frequencia, 5000)
    else:
        print(f"Frequência para {animal} não encontrada.")


def beep(frequency, duration):
    os.system(f"play -n synth {duration / 1000} sin {frequency}")


while True:  # Laço infinito
    resposta = input("O peixe está presente? (sim/não/adicionar): ").strip().lower()

    if resposta == "sim":
        animal = input('Qual animal: ').strip().lower()
        disparar_som(animal)
    elif resposta == "adicionar":
        # Adicionar novo animal via API
        novo_animal = input("Digite o nome do novo animal: ").strip().lower()
        nova_frequencia = int(input("Digite a frequência para esse animal: "))
        response = requests.post(f'{API_URL}/adicionar', json={'animal': novo_animal, 'frequencia': nova_frequencia})
        print(response.json()['message'])
    else:
        print("Nenhum som foi disparado.")
