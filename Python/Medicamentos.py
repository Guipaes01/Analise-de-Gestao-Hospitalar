import pandas as pd
import random

random.seed(42)

CAMINHO = r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\medicamentos_estoque.csv"

medicamentos = [
    ("Paracetamol", "Não"),
    ("Dipirona", "Não"),
    ("Amoxicilina", "Não"),
    ("Azitromicina", "Não"),
    ("Ibuprofeno", "Não"),
    ("Omeprazol", "Não"),
    ("Insulina", "Sim"),
    ("Morfina", "Sim"),
    ("Diazepam", "Sim"),
    ("Clonazepam", "Sim"),
    ("Losartana", "Não"),
    ("AAS", "Não"),
    ("Metformina", "Não"),
    ("Atorvastatina", "Não"),
    ("Tramadol", "Sim")
]

municipios = ["Campo Grande", "Dourados", "Três Lagoas", "Corumbá"]

dados = []
medicamento_id = 1

for nome, controlado in medicamentos:
    for municipio in municipios:
        dados.append({
            "medicamento_id": medicamento_id,
            "nome_medicamento": nome,
            "medicamento_controlado": controlado,
            "municipio": municipio,
            "quantidade_estoque": random.randint(50, 1200),
            "estoque_minimo": random.randint(80, 200),
            "custo_unitario": round(random.uniform(2.5, 180), 2)
        })
        medicamento_id += 1

df = pd.DataFrame(dados)
df.to_csv(CAMINHO, index=False, encoding="utf-8")

print("Arquivo medicamentos_estoque.csv gerado com sucesso!")
