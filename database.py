import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

if __name__ == "__main__":
    connection = get_connection()
    print ("Connected to MySQL!")
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tickets")
    results = cursor.fetchall()
    for row in results:
        print (row)
    connection.close()