import json

with open('assets/faturamento_mensal.json', 'r') as json_file:
    raw_data = json.load(json_file)

    filtered_data = [d for d in raw_data if d["valor"] != 0.0]

json_file.close()

# Retorno do maior e menor faturamento ocorrido em um dia do mês:

max_value = max(filtered_data, key=lambda revenue: revenue["valor"])
min_value = min(filtered_data, key=lambda revenue: revenue["valor"])

print(
    f'O menor valor de faturamento ocorrido em um dia do mês: R$ {min_value}')
print(
    f'O maior valor de faturamento ocorrido em um dia do mês: R$ {max_value}')

# Retorno do número de dias do mês em que o valor de faturamento
# diário foi superior à média mensal:

total_days = len(filtered_data)
total_sum = sum([revenue["valor"] for revenue in filtered_data])

monthly_avarage = total_sum / total_days

higher_than_monthly_avarage = [
    revenue["valor"]
    for revenue in filtered_data if revenue["valor"] > monthly_avarage
]

amount = len(higher_than_monthly_avarage)

print(
    f'Número de dias no mês em que o valor de faturamento diário foi superior '
    f'à média mensal: {amount}')
