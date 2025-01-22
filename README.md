Sistema de Gestão de Reservas de Passagens Aéreas - Companhia Aérea
Este projeto consiste em um sistema de gestão de reservas de passagens aéreas para uma companhia aérea. O sistema é composto por um banco de dados MySQL e um CRUD em Python, permitindo que o usuário execute operações básicas de criação, leitura, atualização e exclusão (CRUD) de reservas, diretamente através do terminal.
Funcionalidades
•	Banco de Dados MySQL: O banco de dados contém várias tabelas para gerenciar informações sobre clientes, voos, reservas e pagamentos.
o	Cliente: Armazena informações pessoais dos clientes, como CPF, RG, nome, email, e outros dados.
o	Voo: Contém os voos disponíveis com detalhes como código, origem, destino e tipo de aeronave.
o	Reserva: Registra as reservas feitas pelos clientes, incluindo dados como código da reserva, status e datas.
o	Pagamento: Armazena as informações de pagamento relacionadas a cada reserva, como operadora de cartão, número de parcelas e valor total.
o	TrechoVoo: Define os trechos dos voos, incluindo horários de partida e chegada e classe (econômica, executiva, ou primeira classe).
o	ReservaTrecho: Relaciona as reservas aos trechos dos voos.
•	CRUD em Python: O CRUD permite que o usuário interaja com o banco de dados para:
o	Criar novas reservas.
o	Ler detalhes de uma reserva existente.
o	Atualizar informações de uma reserva, como CPF, status, e datas.
o	Deletar reservas do banco de dados.
Funcionalidades do CRUD:
1.	Criar Reserva: Insere uma nova reserva no banco de dados, associando um cliente a um voo com a data e o status da reserva.
2.	Ler Reserva: Permite consultar uma reserva existente utilizando o código da reserva.
3.	Atualizar Reserva: Permite modificar os detalhes de uma reserva, incluindo o CPF, status e datas de validade.
4.	Deletar Reserva: Permite excluir uma reserva do banco de dados.
Tecnologias Utilizadas
•	MySQL: Banco de dados relacional para armazenar as informações da companhia aérea, como voos, clientes, reservas e pagamentos.
•	Python: Linguagem utilizada para criar o CRUD que interage com o banco de dados, permitindo a manipulação das reservas via terminal.
•	mysql.connector: Biblioteca Python utilizada para conectar e interagir com o banco de dados MySQL.
Como Executar
1.	Configuração do Banco de Dados:
o	Certifique-se de ter o MySQL instalado e configurado em sua máquina.
o	Crie o banco de dados e as tabelas usando o script SQL fornecido.
2.	Configuração do Python:
o	Instale o Python e a biblioteca mysql.connector utilizando o seguinte comando:
bash
CopiarEditar
pip install mysql-connector-python
3.	Executando o CRUD:
o	Após configurar o banco de dados, execute o script crud.py para acessar o menu interativo e gerenciar as reservas.
bash
CopiarEditar
python crud.py
4.	Interação via Terminal:
o	O menu permitirá ao usuário criar, ler, atualizar ou deletar reservas, além de exibir mensagens de sucesso ou erro conforme a operação realizada.
Exemplo de Uso
1.	Criar Reserva:
o	O usuário será solicitado a fornecer um código de reserva, CPF, status e as datas de reserva e validade.
2.	Ler Reserva:
o	O usuário poderá consultar informações de uma reserva ao informar o código da reserva.
3.	Atualizar Reserva:
o	O usuário poderá modificar detalhes de uma reserva existente, como CPF, status ou datas.
4.	Deletar Reserva:
o	O usuário poderá excluir uma reserva informando o código da reserva.

