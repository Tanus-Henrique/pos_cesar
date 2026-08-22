"""
Atividade: Análise de Dados da API NASA DONKI - Explosões Solares

Aluno: Seu Nome Aqui
Turma: Sua Turma Aqui

Objetivo:
Consumir dados da API pública da NASA DONKI, carregar os dados de explosões solares
em um DataFrame do Pandas e realizar uma análise inicial com tratamento e limpeza.
"""

# ============================================================
# 1. Importação das bibliotecas
# ============================================================

import requests
import pandas as pd
import json


# ============================================================
# 2. Configuração da API
# ============================================================

# Endpoint da API DONKI para explosões solares (Solar Flares)
url = "https://api.nasa.gov/DONKI/FLR"

# Parâmetros da requisição
params = {
    "startDate": "2026-01-01",
    "endDate": "2026-12-30",
    "api_key": "DEMO_KEY"
}


# ============================================================
# 3. Requisição GET para a API da NASA
# ============================================================

response = requests.get(url, params=params)

print("Status code:", response.status_code)
print("Limite de requisições:", response.headers.get("X-RateLimit-Limit"))
print("Requisições restantes:", response.headers.get("X-RateLimit-Remaining"))

# Caso a API retorne erro, esta linha interrompe a execução e mostra o erro
response.raise_for_status()


# ============================================================
# 4. Carregamento dos dados em JSON
# ============================================================

dados = response.json()

print("\nTipo dos dados retornados:", type(dados))
print("Quantidade de registros:", len(dados))

# Exibe o primeiro registro para entender a estrutura dos dados
if len(dados) > 0:
    print("\nPrimeiro registro retornado pela API:")
    print(json.dumps(dados[0], indent=4, ensure_ascii=False))
else:
    print("\nNenhum dado retornado para o período informado.")


# ============================================================
# 5. Criação do DataFrame com Pandas
# ============================================================

# json_normalize ajuda a transformar dados JSON, inclusive aninhados, em tabela
df = pd.json_normalize(dados)

print("\nPrimeiras linhas do DataFrame:")
print(df.head())


# ============================================================
# 6. Inspeção inicial dos dados
# ============================================================

print("\nFormato do DataFrame:")
print(df.shape)

print("\nColunas disponíveis:")
print(df.columns.tolist())

print("\nInformações gerais:")
print(df.info())

print("\nValores ausentes por coluna:")
print(df.isna().sum().sort_values(ascending=False))


# ============================================================
# 7. Tratamento e limpeza dos dados
# ============================================================

# Cria uma cópia para manter o DataFrame original preservado
df_limpo = df.copy()

# Remove duplicatas usando somente colunas simples.
# Algumas colunas da API vêm como listas/dicionários, como instruments e linkedEvents.
# Essas colunas podem gerar erro "TypeError: unhashable type: 'list'" no drop_duplicates().
colunas_para_duplicatas = [
    "flrID",
    "beginTime",
    "peakTime",
    "endTime",
    "classType",
    "sourceLocation",
    "activeRegionNum"
]

colunas_existentes = [
    coluna for coluna in colunas_para_duplicatas
    if coluna in df_limpo.columns
]

df_limpo = df_limpo.drop_duplicates(subset=colunas_existentes)

# Converte colunas de data/hora para datetime, caso existam
colunas_data = ["beginTime", "peakTime", "endTime"]

for coluna in colunas_data:
    if coluna in df_limpo.columns:
        df_limpo[coluna] = pd.to_datetime(df_limpo[coluna], errors="coerce")

# Cria uma coluna apenas com a data do evento
if "beginTime" in df_limpo.columns:
    df_limpo["data_evento"] = df_limpo["beginTime"].dt.date

# Calcula a duração do evento em minutos, quando possível
if "beginTime" in df_limpo.columns and "endTime" in df_limpo.columns:
    df_limpo["duracao_minutos"] = (
        df_limpo["endTime"] - df_limpo["beginTime"]
    ).dt.total_seconds() / 60

# Trata o campo instruments, que pode vir como lista de dicionários
if "instruments" in df_limpo.columns:
    df_limpo["instrumentos"] = df_limpo["instruments"].apply(
        lambda lista: ", ".join(
            [item.get("displayName", "") for item in lista]
        ) if isinstance(lista, list) else None
    )

print("\nDataFrame após tratamento:")
print(df_limpo.head())


# ============================================================
# 8. Análise exploratória inicial
# ============================================================

print("\nTotal de explosões solares registradas:", len(df_limpo))

# Frequência por classe da explosão solar
if "classType" in df_limpo.columns and not df_limpo.empty:
    print("\nQuantidade de eventos por classe:")
    print(df_limpo["classType"].value_counts())
else:
    print("\nColuna classType não encontrada ou DataFrame vazio.")

# Quantidade de eventos por mês
if "beginTime" in df_limpo.columns and not df_limpo.empty:
    eventos_por_mes = (
        df_limpo
        .assign(mes=df_limpo["beginTime"].dt.to_period("M"))
        .groupby("mes")
        .size()
        .reset_index(name="quantidade")
    )

    print("\nQuantidade de eventos por mês:")
    print(eventos_por_mes)
else:
    print("\nNão foi possível calcular eventos por mês.")

# Estatísticas da duração dos eventos
if "duracao_minutos" in df_limpo.columns and not df_limpo["duracao_minutos"].dropna().empty:
    print("\nEstatísticas da duração dos eventos em minutos:")
    print(df_limpo["duracao_minutos"].describe())
else:
    print("\nNão foi possível calcular estatísticas de duração.")


# ============================================================
# 9. Visualizações simples
# ============================================================

# Gráfico de eventos por classe
if "classType" in df_limpo.columns and not df_limpo.empty:
    df_limpo["classType"].value_counts().plot(
        kind="bar",
        title="Quantidade de explosões solares por classe",
        xlabel="Classe",
        ylabel="Quantidade",
        figsize=(10, 5)
    )

# Para evitar sobreposição de gráficos quando rodar em script
try:
    import matplotlib.pyplot as plt

    if "classType" in df_limpo.columns and not df_limpo.empty:
        plt.tight_layout()
        plt.show()

    # Gráfico de eventos por mês
    if "beginTime" in df_limpo.columns and not df_limpo.empty:
        eventos_por_mes_plot = (
            df_limpo
            .assign(mes=df_limpo["beginTime"].dt.to_period("M").astype(str))
            .groupby("mes")
            .size()
        )

        eventos_por_mes_plot.plot(
            kind="bar",
            title="Quantidade de explosões solares por mês",
            xlabel="Mês",
            ylabel="Quantidade",
            figsize=(10, 5)
        )

        plt.tight_layout()
        plt.show()

except ImportError:
    print("\nMatplotlib não está instalado. Os gráficos não foram exibidos.")


# ============================================================
# 10. Observações sobre os dados coletados
# ============================================================

print("""
Observações sobre os dados:

1. O dataset foi obtido diretamente da API pública da NASA DONKI.
2. Os dados retornam informações sobre explosões solares, como horário de início,
   horário de pico, horário de término, classe da explosão e instrumentos usados.
3. As colunas de data foram convertidas para datetime para facilitar análises temporais.
4. A coluna classType permite observar a intensidade das explosões solares.
5. O campo instruments possui dados aninhados, por isso foi criada a coluna instrumentos.
6. Caso a API retorne poucos ou nenhum registro, isso pode acontecer porque o período
   informado contém datas futuras ou porque não há registros disponíveis no intervalo.
7. A DEMO_KEY é suficiente para testes, mas possui limite reduzido de requisições.
""")


# ============================================================
# 11. Salvando o resultado tratado
# ============================================================

df_limpo.to_csv("nasa_donki_flr_tratado.csv", index=False)

print("\nArquivo CSV salvo com sucesso: nasa_donki_flr_tratado.csv")
