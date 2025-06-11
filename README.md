# Vaapty - Scripts de Automação via PyCharm

Este repositório contém exemplos de automações desenvolvidas com foco em otimizar tarefas diárias, melhorar a **gestão de dados** e **comunicações**. 

## Scripts:

### 1. `separar_clientes_por_contato.py`
Esse script lê a planilha **`CLIENTES_EXEMPLO.xlsx`** e divide os dados em **4 arquivos** com base na presença de e-mail e telefone:
- **clientes_com_email_telefone.xlsx**: Contém clientes com ambos os dados.
- **clientes_so_email.xlsx**: Contém clientes com apenas e-mail.
- **clientes_so_telefone.xlsx**: Contém clientes com apenas telefone.
- **clientes_sem_contato.xlsx**: Contém clientes sem nenhum contato.

### 2. `enviar_email_html_clientes.py`
Envia um **e-mail HTML** para uma lista de clientes que possuem e-mail, com a tabela contendo nome, e-mail e telefone, ideal para campanhas de marketing ou validações manuais.

## Requisitos:
Para rodar os scripts, é necessário ter o Python instalado em sua máquina e as bibliotecas listadas no arquivo **`requirements.txt`**.

### Dependências:
- Python 3.8+
- pandas
- openpyxl
- smtplib (biblioteca nativa do Python)

## Como Usar:

### 1. Instalar dependências:
Abra o terminal (ou terminal integrado no PyCharm) e rode o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install -r requirements.txt

2. Executar os Scripts:
Após instalar as dependências, você pode rodar qualquer um dos scripts com o seguinte comando:
python nome_do_script.py



🤝 Contribuindo
Se você quiser colaborar com o projeto, fique à vontade para enviar pull requests ou issues diretamente no GitHub. Suas contribuições são bem-vindas!
