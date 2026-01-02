import pandas as pd
import random

cargos = {
    "MEDICO": (12000, 28000),
    "ENFERMEIRO": (4500, 9000),
    "TECNICO ENFERMAGEM": (2500, 4500),
    "ADMINISTRATIVO": (3000, 6000)
}

unidades = [
    (1, "HOSPITAL CENTRAL"),
    (2, "HOSPITAL REGIONAL"),
    (3, "UPA NORTE"),
    (4, "UPA SUL"),
    (5, "CLINICA MUNICIPAL")
]

dados = []
profissional_id = 1

for id_unidade, unidade in unidades:
    for cargo, faixa in cargos.items():
        for _ in range(random.randint(5, 15)):
            dados.append({
                "profissional_id": profissional_id,
                "cargo": cargo,
                "id_unidade": id_unidade,
                "unidade": unidade,
                "salario_mensal": round(random.uniform(*faixa), 2),
                "carga_horaria_semanal": random.choice([20, 30, 40])
            })
            profissional_id += 1

df = pd.DataFrame(dados)

df.to_csv(
    r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\salarios_profissionais.csv",
    index=False,
    encoding="utf-8"
)
