import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

df = pd.read_excel("CLIENTES_EXEMPLO.xlsx")
clientes = df.dropna(subset=["Email"])  # apenas quem tem email

tabela_html = clientes[["Nome", "Email", "Telefone"]].to_html(index=False)

mensagem = MIMEMultipart("alternative")
mensagem["Subject"] = "Lista de Clientes com E-mail"
mensagem["From"] = "seuemail@vaapty.com"
mensagem["To"] = "destinatario@vaapty.com"
mensagem.attach(MIMEText(tabela_html, "html"))

with smtplib.SMTP("smtp.seudominio.com", 587) as server:
    server.starttls()
    server.login("seuemail@vaapty.com", "sua_senha")
    server.send_message(mensagem)