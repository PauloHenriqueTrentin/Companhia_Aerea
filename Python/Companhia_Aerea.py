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

def update_reserva(codigo_reserva, cpf=None, status=None, data_reserva=None, data_validade=None):
    """
    UPDATE
    Função para atualizar uma reserva no banco de dados.
    UPDATE
    """
    conexao = create_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            update_query = "UPDATE Reserva SET "
            updates = []
            params = []
            
            if cpf:
                updates.append("CPF = %s")
                params.append(cpf)
            if status:
                updates.append("Status = %s")
                params.append(status)
            if data_reserva:
                updates.append("DataReserva = %s")
                params.append(data_reserva)
            if data_validade:
                updates.append("DataValidade = %s")
                params.append(data_validade)
            
            update_query += ", ".join(updates)
            update_query += " WHERE CodigoReserva = %s"
            params.append(codigo_reserva)

            cursor.execute(update_query, tuple(params))
            conexao.commit()
            print("Reserva atualizada com sucesso!")
        except Error as e:
            print(f"Erro ao atualizar reserva: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexao.close()

def delete_reserva(codigo_reserva):
    """
    DELETE
    Função para deletar uma reserva do banco de dados.
    DELETE
    """
    conexao = create_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            delete_query = "DELETE FROM Reserva WHERE CodigoReserva = %s"
            cursor.execute(delete_query, (codigo_reserva,))
            conexao.commit()
            print("Reserva deletada com sucesso!")
        except Error as e:
            print(f"Erro ao deletar reserva: {e}")
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexao.close()

