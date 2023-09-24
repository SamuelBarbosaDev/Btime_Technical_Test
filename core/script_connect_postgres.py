import psycopg2


def connect_postgres(
    dbname: str = None,
    user: str = None,
    password: str = None,
    host: str = None,
    port: str = None,
):
    # Parâmetros de conexão com o banco de dados PostgreSQL
    db_params = {
        'dbname': dbname,
        'user': user,
        'password': password,
        'host': host,
        'port': port,
    }
    # Tentar estabelecer uma conexão com o banco de dados
    try:
        # Estabelecer a conexão com o banco de dados
        conn = psycopg2.connect(**db_params)

    except psycopg2.Error as e:
        print("Erro ao conectar ao banco de dados:", e)

    return conn
