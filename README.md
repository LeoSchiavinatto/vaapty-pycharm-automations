# Vaapty - Scripts de Automação via PyCharm

Este repositório contém exemplos de automações desenvolvidas para a Vaapty Franchising com foco em:

## Scripts:

### 1. `separar_clientes_por_contato.py`
Esse script lê a planilha `CLIENTES_EXEMPLO.xlsx` e divide os dados em 4 arquivos com base na presença de e-mail e telefone:
- `clientes_com_email_telefone.xlsx`
- `clientes_so_email.xlsx`
- `clientes_so_telefone.xlsx`
- `clientes_sem_contato.xlsx`

### 2. `enviar_email_html_clientes.py`
Envia um e-mail HTML com a lista de clientes que possuem e-mail, em formato de tabela.

## Requisitos
- Python 3.8+
- pandas
- openpyxl
- smtplib (biblioteca nativa)

## Como usar
1. Abra o terminal e instale os requisitos com `pip install pandas openpyxl`.
2. Execute o script desejado com `python nome_do_script.py`.

---

*Este projeto foi desenvolvido para fins demonstrativos e pode ser adaptado conforme a necessidade da franqueadora.*