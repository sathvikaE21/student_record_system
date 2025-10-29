import mysql.connector

DB_CONFIG = {
    'host': 'host.docker.internal',
    'port': 3306,
    'user': 'root',
    'password': 'chikky21#',
    'database': 'std_db'
}

def get_db_connection():
    print("Connecting to MySQL with:", DB_CONFIG)
    return mysql.connector.connect(**DB_CONFIG)