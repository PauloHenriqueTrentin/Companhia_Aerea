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

