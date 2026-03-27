import requests
import time

base_url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/{}'

todos_resultados = []

for concurso in range(1, 2700):  # ajuste conforme necessário
    try:
        url = base_url.format(concurso)
        response = requests.get(url)

        if response.status_code != 200:
            print(f'Concurso {concurso} não encontrado')
            continue

        data = response.json()

        resultado = {
            'concurso': data['numero'],
            'data': data['dataApuracao'],
            'dezenas': data['listaDezenas']
        }

        todos_resultados.append(resultado)

        print(f'✔ Concurso {concurso} coletado')

        time.sleep(0.2)  # evita sobrecarregar a API

    except Exception as e:
        print(f'Erro no concurso {concurso}: {e}')