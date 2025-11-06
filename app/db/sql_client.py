# app/db/mysql_client.py
import os
import pymysql
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -------------------------------
# 1️⃣ Get MySQL connection
# -------------------------------
def get_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),  # default MySQL port
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""), # blank if no password
        database=os.getenv("DB_NAME", "palm_rag"),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# -------------------------------
# 2️⃣ Save document metadata
# -------------------------------
def save_document_metadata(document_id: str, file_name: str, file_type: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO documents (document_id, file_name, file_type) VALUES (%s, %s, %s)"
            cursor.execute(sql, (document_id, file_name, file_type))
        conn.commit()
    finally:
        conn.close()

# -------------------------------
# 3️⃣ Save chunk metadata
# -------------------------------
def save_chunk_metadata(chunk_id: str, document_id: str, chunk_index: int, chunk_text: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO chunks (chunk_id, document_id, chunk_index, chunk_text) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (chunk_id, document_id, chunk_index, chunk_text))
        conn.commit()
    finally:
        conn.close()
