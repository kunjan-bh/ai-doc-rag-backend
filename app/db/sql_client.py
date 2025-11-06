# app/db/mysql_client.py
import os
import pymysql
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()


def get_connection():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)), 
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""), 
        database=os.getenv("DB_NAME", "palm_rag"),
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection


def save_document_metadata(document_id: str, file_name: str, file_type: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO documents (document_id, file_name, file_type) VALUES (%s, %s, %s)"
            cursor.execute(sql, (document_id, file_name, file_type))
        conn.commit()
    finally:
        conn.close()


def save_chunk_metadata(chunk_id: str, document_id: str, chunk_index: int, chunk_text: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO chunks (chunk_id, document_id, chunk_index, chunk_text) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (chunk_id, document_id, chunk_index, chunk_text))
        conn.commit()
    finally:
        conn.close()

def save_booking(name: str, email: str, date: str, time: str):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO bookings (name, email, date, time, created_at)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (name, email, date, time, datetime.now()))
        conn.commit()
    finally:
        conn.close()


def get_all_bookings():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM bookings ORDER BY created_at DESC")
            return cursor.fetchall()
    finally:
        conn.close()