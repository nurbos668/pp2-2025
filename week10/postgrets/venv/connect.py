import psycopg2
from config import load_config

def connect(config):
    """Подключение к серверу PostgreSQL"""
    try:
        # Подключение к серверу PostgreSQL
        with psycopg2.connect(**config) as conn:
            print('Подключение к серверу PostgreSQL установлено.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    config = load_config()
    connect(config)
