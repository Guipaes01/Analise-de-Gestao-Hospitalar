import pandas as pd
import random

anos = [2021, 2022, 2023]
meses = range(1, 13)
categorias = ["Energia", "Agua", "Manutencao", "Limpeza", "Seguranca"]
unidades = [
    (1, "HOSPITAL CENTRAL"),
    (2, "HOSPITAL REGIONAL"),
    (3, "UPA NORTE"),
    (4, "UPA SUL"),
    (5, "CLINICA MUNICIPAL")
]

dados = []
custo_id = 1

for ano in anos:
    for mes in meses:
        for id_unidade, unidade in unidades:
            for categoria in categorias:
                dados.append({
                    "custo_id": custo_id,
                    "ano": ano,
                    "mes": mes,
                    "id_unidade": id_unidade,
                    "unidade": unidade,
                    "categoria": categoria,
                    "valor": round(random.uniform(5000, 40000), 2)
                })
                custo_id += 1

df = pd.DataFrame(dados)

df.to_csv(
    r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\custos_fixos.csv",
    index=False,
    encoding="utf-8"
)
