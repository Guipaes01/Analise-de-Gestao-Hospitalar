import pandas as pd

custos = pd.read_csv(r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\custos_fixos.csv")
salarios = pd.read_csv(r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\salarios_profissionais.csv")

unidades = pd.concat(
    [custos["unidade"], salarios["municipio"]],
    ignore_index=True
).astype(str).str.strip().str.upper().drop_duplicates()

dim_unidade = pd.DataFrame({
    "id_unidade": range(1, len(unidades) + 1),
    "unidade": unidades.values
})

dim_unidade.to_csv(
    r"C:\Users\guilh\OneDrive\Documentos\Saude\CSV\dim_unidade.csv",
    index=False
)
