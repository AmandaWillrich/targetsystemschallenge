revenue = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(revenue.values())

for state, value in revenue.items():
    percent = (value / total) * 100
    print(f'{state}: {percent:.2f}%')
