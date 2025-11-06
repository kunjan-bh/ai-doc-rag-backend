-- ==========================================
-- PalmMind RAG Backend - Database Schema
-- ==========================================

-- 1️⃣ Create database
CREATE DATABASE IF NOT EXISTS palm_rag;
USE palm_rag;

-- 2️⃣ Documents table
CREATE TABLE IF NOT EXISTS documents (
    document_id VARCHAR(36) PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(10) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3️⃣ Chunks table
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id VARCHAR(36) PRIMARY KEY,
    document_id VARCHAR(36),
    chunk_index INT,
    chunk_text TEXT,
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);

-- ==========================================
-- Example inserts (optional)
-- INSERT INTO documents (document_id, file_name, file_type)
-- VALUES ('123e4567-e89b-12d3-a456-426614174000', 'example.pdf', 'pdf');
-- 
-- INSERT INTO chunks (chunk_id, document_id, chunk_index, chunk_text)
-- VALUES ('223e4567-e89b-12d3-a456-426614174001', '123e4567-e89b-12d3-a456-426614174000', 0, 'This is the first chunk text.');
-- ==========================================
