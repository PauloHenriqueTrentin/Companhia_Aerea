import mysql.connector
from mysql.connector import Error

def create_connection():
    """
    CONEXAO
    Função para criar uma conexão com o banco de dados MySQL.
    CONEXAO
    
    Returns:
        mysql.connector.connection.MySQLConnection: Objeto de conexão se a conexão for bem-sucedida, None caso contrário.
    """
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='samsung11',
            database='bosta'
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def create_reserva(codigo_reserva, cpf, status, data_reserva, data_validade):
    """
    CREATE
    Função para inserir uma nova reserva no banco de dados.
    CREATE
    """
    conexao = create_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            insert_query = """
            INSERT INTO Reserva (CodigoReserva, CPF, Status, DataReserva, DataValidade)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (codigo_reserva, cpf, status, data_reserva, data_validade))
            conexao.commit()
            print("Reserva criada com sucesso!")
        except Error as e:
            print(f"Erro ao inserir reserva: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexao.close()

def read_reserva(codigo_reserva):
    """
    READ
    Função para ler uma reserva do banco de dados baseado no código da reserva.
    READ
    """
    conexao = create_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            select_query = "SELECT * FROM Reserva WHERE CodigoReserva = %s"
            cursor.execute(select_query, (codigo_reserva,))
            reserva = cursor.fetchone()
            return reserva
        except Error as e:
            print(f"Erro ao ler reserva: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexao.close()

