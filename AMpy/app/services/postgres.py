import pandas as pd
import psycopg2
from app.config.settings import PG_CONFIG

def executar_query(query):
    conn_str = (
        f"host={PG_CONFIG['host']} "
        f"port={PG_CONFIG['port']} "
        f"dbname={PG_CONFIG['dbname']} "
        f"user={PG_CONFIG['user']} "
        f"password={PG_CONFIG['password']}"
    )
    conn = psycopg2.connect(conn_str)
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df


## Exemplo de uso

# if __name__ == "__main__":
#     query = input("Digite sua query SQL: ")

#     df_resultado = executar_query(
#         query_sql=query,
#         host="localhost",
#         database="meu_banco",
#         user="meu_usuario",
#         password="minha_senha"
#     )

#     print("Resultado:")
#     print(df_resultado)
