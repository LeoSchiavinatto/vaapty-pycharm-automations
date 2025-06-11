import pandas as pd

df = pd.read_excel("CLIENTES_EXEMPLO.xlsx")

# Garantir que colunas relevantes existam
df = df[["Nome", "DataCompra", "Email", "Telefone"]]

ambos = df[df["Email"].notna() & df["Telefone"].notna()]
so_email = df[df["Email"].notna() & df["Telefone"].isna()]
so_telefone = df[df["Email"].isna() & df["Telefone"].notna()]
nenhum = df[df["Email"].isna() & df["Telefone"].isna()]

ambos.to_excel("clientes_com_email_telefone.xlsx", index=False)
so_email.to_excel("clientes_so_email.xlsx", index=False)
so_telefone.to_excel("clientes_so_telefone.xlsx", index=False)
nenhum.to_excel("clientes_sem_contato.xlsx", index=False)