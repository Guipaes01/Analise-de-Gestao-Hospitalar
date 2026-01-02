import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker("pt_BR")
random.seed(42)

# CONFIGURAÇÕES
CAMINHO = r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\atendimentos.csv"
DATA_INICIO = datetime(2021, 1, 1)
DATA_FIM = datetime(2023, 12, 31)

TIPOS = ["Consulta", "Exame", "Emergência"]
ESPECIALIDADES = ["Clínica Médica", "Pediatria", "Ortopedia", "Cardiologia"]
ORIGENS = ["SUS", "Convênio", "Particular"]
MUNICIPIOS = ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá"]

dados = []
atendimento_id = 1

for paciente_id in range(1, 301):
    qtd = random.randint(1, 15)
    municipio = random.choice(MUNICIPIOS)

    for _ in range(qtd):
        tipo = random.choice(TIPOS)
        origem = random.choices(ORIGENS, weights=[55, 30, 15])[0]

        if tipo == "Consulta":
            custo = random.uniform(80, 180)
        elif tipo == "Exame":
            custo = random.uniform(150, 400)
        else:
            custo = random.uniform(300, 900)

        dados.append({
            "atendimento_id": atendimento_id,
            "paciente_id": paciente_id,
            "data_atendimento": fake.date_between(DATA_INICIO, DATA_FIM),
            "tipo_atendimento": tipo,
            "especialidade": random.choice(ESPECIALIDADES),
            "municipio": municipio,
            "custo_atendimento": round(custo, 2),
            "origem": origem
        })

        atendimento_id += 1

df = pd.DataFrame(dados)
df.to_csv(CAMINHO, index=False, encoding="utf-8")

print("Arquivo atendimentos.csv gerado com sucesso!")
