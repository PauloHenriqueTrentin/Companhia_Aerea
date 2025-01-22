# ✈️ Sistema de Gestão de Reservas de Passagens Aéreas - Companhia Aérea

Este projeto consiste em um sistema de gestão de reservas de passagens aéreas para uma companhia aérea. O sistema é composto por um banco de dados MySQL e um CRUD em Python, permitindo que o usuário execute operações básicas de criação, leitura, atualização e exclusão (CRUD) de reservas, diretamente através do terminal.

## Funcionalidades

### Banco de Dados MySQL
O banco de dados contém várias tabelas para gerenciar informações sobre clientes, voos, reservas e pagamentos:

- **Cliente**: Armazena informações pessoais dos clientes, como CPF, RG, nome, email, e outros dados.
- **Voo**: Contém os voos disponíveis com detalhes como código, origem, destino e tipo de aeronave.
- **Reserva**: Registra as reservas feitas pelos clientes, incluindo dados como código da reserva, status e datas.
- **Pagamento**: Armazena as informações de pagamento relacionadas a cada reserva, como operadora de cartão, número de parcelas e valor total.
- **TrechoVoo**: Define os trechos dos voos, incluindo horários de partida e chegada e classe (econômica, executiva, ou primeira classe).
- **ReservaTrecho**: Relaciona as reservas aos trechos dos voos.

### CRUD em Python
O CRUD permite que o usuário interaja com o banco de dados para:

- **Criar novas reservas**.
- **Ler detalhes de uma reserva existente**.
- **Atualizar informações de uma reserva**, como CPF, status, e datas.
- **Deletar reservas do banco de dados**.

#### Funcionalidades do CRUD:
- **Criar Reserva**: Insere uma nova reserva no banco de dados, associando um cliente a um voo com a data e o status da reserva.
- **Ler Reserva**: Permite consultar uma reserva existente utilizando o código da reserva.
- **Atualizar Reserva**: Permite modificar os detalhes de uma reserva, incluindo o CPF, status e datas de validade.
- **Deletar Reserva**: Permite excluir uma reserva do banco de dados.

## Tecnologias Utilizadas
- **MySQL**: Banco de dados relacional para armazenar as informações da companhia aérea, como voos, clientes, reservas e pagamentos.
- **Python**: Linguagem utilizada para criar o CRUD que interage com o banco de dados, permitindo a manipulação das reservas via terminal.
- **mysql.connector**: Biblioteca Python utilizada para conectar e interagir com o banco de dados MySQL.
