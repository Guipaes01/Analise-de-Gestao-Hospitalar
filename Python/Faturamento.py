import pandas as pd
import random
from faker import Faker
from datetime import datetime

fake = Faker("pt_BR")
random.seed(42)

CAMINHO = r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\faturamento.csv"

DATA_INICIO = datetime(2021, 1, 1)
DATA_FIM = datetime(2023, 12, 31)

municipios = ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá"]
origens = ["SUS", "Convênio", "Particular"]
procedimentos = ["Consulta", "Exame", "Emergência"]

dados = []
faturamento_id = 1

for _ in range(4500):
    origem = random.choices(origens, weights=[55, 30, 15])[0]
    procedimento = random.choice(procedimentos)

    if origem == "SUS":
        valor = random.uniform(60, 220)
    elif origem == "Convênio":
        valor = random.uniform(150, 480)
    else:
        valor = random.uniform(200, 850)

    dados.append({
        "faturamento_id": faturamento_id,
        "data_faturamento": fake.date_between(DATA_INICIO, DATA_FIM),
        "municipio": random.choice(municipios),
        "origem": origem,
        "procedimento": procedimento,
        "valor_receita": round(valor, 2)
    })

    faturamento_id += 1

df = pd.DataFrame(dados)
df.to_csv(CAMINHO, index=False, encoding="utf-8")

print("Arquivo faturamento.csv gerado com sucesso!")
