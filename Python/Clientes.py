import pandas as pd
import random
from faker import Faker
from datetime import date

# Configurações
fake = Faker("pt_BR")
random.seed(42)

N_REGISTROS = 300
municipios = ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá"]
sexos = ["Masculino", "Feminino"]

dados = []

for i in range(1, N_REGISTROS + 1):
    data_nascimento = fake.date_of_birth(minimum_age=0, maximum_age=95)
    idade = date.today().year - data_nascimento.year

    if idade <= 12:
        faixa_etaria = "Criança"
    elif idade <= 17:
        faixa_etaria = "Adolescente"
    elif idade <= 59:
        faixa_etaria = "Adulto"
    else:
        faixa_etaria = "Idoso"

    dados.append({
        "paciente_id": i,
        "nome": fake.name(),
        "sexo": random.choice(sexos),
        "data_nascimento": data_nascimento.strftime("%Y-%m-%d"),
        "idade": idade,
        "faixa_etaria": faixa_etaria,
        "municipio": random.choice(municipios),
        "possui_plano_saude": random.choices(
            ["Sim", "Não"], weights=[45, 55]
        )[0]
    })

df = pd.DataFrame(dados)

df.to_csv(
    r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\pacientes.csv",
    index=False,
    encoding="utf-8"
)

print("Arquivo pacientes.csv gerado com sucesso!")

