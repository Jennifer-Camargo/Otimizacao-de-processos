import pandas as pd

# Simulação de carregamento de dados de qualidade
data = {'medida': [10.2, 10.5, 9.8, 12.1, 10.3, 9.9, 11.5]}
df = pd.DataFrame(data)

# Cálculo de métricas essenciais da Qualidade
media = df['medida'].mean()
desvio_padrao = df['medida'].std()

print(f"Média do Processo: {media:.2f}")
print(f"Variabilidade (Desvio Padrão): {desvio_padrao:.2f}")

# Regra de 3 sigmas (Controle Estatístico de Processo)
limite_superior = media + (3 * desvio_padrao)
limite_inferior = media - (3 * desvio_padrao)

print(f"O processo deve operar entre {limite_inferior:.2f} e {limite_superior:.2f}")
