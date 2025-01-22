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

def menu():
    """
    MENU
    Função que exibe um menu interativo para gerenciar reservas.
    MENU
    """
    while True:
        print("\nMenu de Reservas:")
        print("1. Criar Reserva")
        print("2. Ler Reserva")
        print("3. Atualizar Reserva")
        print("4. Deletar Reserva")
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            codigo_reserva = input("Digite o código da reserva: ")
            cpf = input("Digite o CPF: ")
            status = input("Digite o status (Efetivada/NaoEfetivada): ")
            data_reserva = input("Digite a data da reserva (AAAA-MM-DD): ")
            data_validade = input("Digite a data de validade (AAAA-MM-DD): ")
            create_reserva(codigo_reserva, cpf, status, data_reserva, data_validade)
        
        elif choice == '2':
            codigo_reserva = input("Digite o código da reserva: ")
            reserva = read_reserva(codigo_reserva)
            if reserva:
                print(f"Reserva encontrada: {reserva}")
            else:
                print("Reserva não encontrada.")
        
        elif choice == '3':
            codigo_reserva = input("Digite o código da reserva: ")
            cpf = input("Digite o novo CPF (ou deixe vazio para não alterar): ")
            status = input("Digite o novo status (ou deixe vazio para não alterar): ")
            data_reserva = input("Digite a nova data da reserva (ou deixe vazio para não alterar): ")
            data_validade = input("Digite a nova data de validade (ou deixe vazio para não alterar): ")
            update_reserva(codigo_reserva, cpf if cpf else None, status if status else None, data_reserva if data_reserva else None, data_validade if data_validade else None)
        
        elif choice == '4':
            codigo_reserva = input("Digite o código da reserva: ")
            delete_reserva(codigo_reserva)
        
        elif choice == '5':
            print("Saindo do programa.")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    menu()
