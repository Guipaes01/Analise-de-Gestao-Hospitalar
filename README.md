# 🏥 Projeto de Gestão Hospitalar e Análise de Dados

Este projeto tem como objetivo demonstrar habilidades em **Análise de Dados, Business Intelligence e apoio à tomada de decisão**, aplicadas ao contexto de **gestão hospitalar**.  
O foco está na análise de **custos operacionais, estoque de medicamentos, recursos humanos, perfil dos pacientes e demanda assistencial**, utilizando dados estruturados e dashboards executivos.

---

## 🎯 Objetivo do Projeto

- Analisar **custos fixos e operacionais** das unidades de saúde
- Identificar **riscos no estoque de medicamentos**
- Avaliar **equilíbrio operacional de equipes de saúde**
- Analisar **disparidade salarial por cargo e unidade**
- Compreender o **perfil dos pacientes e a demanda por serviços**
- Criar um **dashboard executivo em Power BI**

---

## 🧱 Estrutura do Projeto

📦 gestao_hospitalar   
┣ 📂 daw   
┃ ┣ 📄 atendimentos.csv    
┃ ┣ 📄 custos_fixos.csv   
┃ ┣ 📄 faturamento.csv   
┃ ┣ 📄 medicamentos_estoque.csv   
┃ ┣ 📄 pacientes.csv   
┃ ┣ 📄 salarios_profissionais.csv   
┃ ┗ 📄 dim_unidade.csv   
┣ 📂 sql   
┃ ┗ 📄 consultas.sql   
┣ 📂 python   
┃ ┗ 📄 geracao_dados.py   
┣ 📂 powerbi   
┃ ┗ 📄 dashboard.pbix   
┗ 📄 README.md   

---

## 🗄️ Modelagem de Dados

O projeto segue o conceito de **modelagem dimensional (modelo estrela)**:

### 🔹 Tabelas Fato
- `atendimentos`
- `custos_fixos`
- `faturamento`
- `medicamentos_estoque`
- `salarios_profissionais`

### 🔹 Tabelas Dimensão
- `dim_unidade`
- `pacientes`

Os relacionamentos são realizados por **id_unidade** e **paciente_id**, garantindo integridade e desempenho analítico.

---

## 🧪 Tecnologias Utilizadas

- **Python** (pandas) — geração e preparação de dados
- **MySQL** — armazenamento e consultas SQL
- **SQL** — análises e agregações
- **Power BI** — modelagem, DAX e visualização de dados
- **Git / GitHub** — versionamento e documentação

---

## 📊 Principais Análises

### 💰 Gestão Financeira
- Variação do custo operacional por ano
- Custo acumulado por unidade
- Resultado operacional (Receita × Custos)

### 📦 Estoque de Medicamentos
- Medicamentos abaixo do estoque mínimo
- Valor parado em estoque
- Índice de cobertura de estoque
- Medicamentos com maior custo de reposição

### 🧑‍⚕️ Recursos Humanos
- Distribuição de médicos e enfermeiros por unidade
- Média salarial por cargo e unidade
- Análise de disparidade salarial entre hospitais e UPAs

### 🧑‍🦱 Perfil do Paciente
- Distribuição por faixa etária
- Percentual de pacientes idosos
- Demanda pediátrica por município
- Proporção de pacientes com e sem plano de saúde

---

## 📈 Dashboard

O dashboard foi desenvolvido no **Power BI**, com foco em:
- Indicadores claros (KPIs)
- Segmentadores globais (Ano, Unidade, Município, Origem)
- Layout moderno com blocos temáticos
- Apoio à tomada de decisão gerencial

O arquivo `.pbix` está disponível na pasta `/powerbi`.
