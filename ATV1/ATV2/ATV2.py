# 1. Função para retornar os números ímpares de uma lista.
def filtrar_impares(lista):
    return [num for num in lista if num % 2 != 0]

# 2. Função para retornar os números primos de uma lista.
def filtrar_primos(lista):
    def is_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    return [num for num in lista if is_primo(num)]

# 3. Função para retornar os elementos que estão presentes em apenas uma das listas.
def elementos_unicos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))

# 4. Função para encontrar o segundo maior valor em uma lista.
def segundo_maior(lista):
    lista_unica = list(set(lista))  # Remove duplicatas
    lista_unica.sort(reverse=True)
    return lista_unica[1]

# 5. Função para ordenar uma lista de tuplas (nome, idade) pelo nome em ordem alfabética.
def ordenar_por_nome(lista):
    return sorted(lista, key=lambda pessoa: pessoa[0])
    

# Exemplo 1
print(filtrar_impares([1, 2, 3, 4, 5]))
# Exemplo 2
print(filtrar_primos([2, 3, 4, 5, 6, 7]))

# Exemplo 3
print(elementos_unicos([1, 2, 3], [2, 3, 4]))

# Exemplo 4
print(segundo_maior([10, 20, 4, 45, 99]))

# Exemplo 5
print(ordenar_por_nome([("Alencar", 30), ("Bruno", 25), ("Carla", 10)]))

# Exemplo 6:
import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(5.5, 3.5), layout="constrained")
for row in range(2):
    for col in range(2):
        axs[row, col].annotate(f'axs[{row}, {col}]', (0.5, 0.5),
                               transform=axs[row, col].transAxes,
                               ha='center', va='center', fontsize=18,
                               color='darkgrey')
fig.suptitle('plt.subplots()')

# Exemplo 7:
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)


# Exemplo 8:
# Usando a variavel df e o import dessa questao para poder responder as questoes 9 e 10 tambem
# import pandas as pd

# Ler o arquivo CSV em um DataFrame
# df = pd.read_csv('nome_do_arquivo.csv')

# Exibir as primeiras linhas (por padrão, as 5 primeiras)
# print(df.head())

# Exemplo 9:
# Selecionar uma coluna específica
# coluna_especifica = df['nome_da_coluna']

# Filtrar linhas onde o valor em 'nome_da_coluna' é maior ou igual que um valor específico
# filtro = df[df['nome_da_coluna'] >= valor_especifico]

# Exemplo 10:
# Remover linhas com valores ausentes
# df_sem_nan = df.dropna()

# Preencher valores ausentes com um valor específico (exemplo: 0)
# df_preenchido = df.fillna(0)

# Preencher valores ausentes com a média da coluna
# df['nome_da_coluna'].fillna(df['nome_da_coluna'].mean(), inplace=True)
