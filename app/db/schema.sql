
CREATE DATABASE IF NOT EXISTS palm_rag;
USE palm_rag;


CREATE TABLE IF NOT EXISTS documents (
    document_id VARCHAR(36) PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_type VARCHAR(10) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS chunks (
    chunk_id VARCHAR(36) PRIMARY KEY,
    document_id VARCHAR(36),
    chunk_index INT,
    chunk_text TEXT,
    FOREIGN KEY (document_id) REFERENCES documents(document_id)
);

CREATE TABLE IF NOT EXISTS chat_sessions (
    session_id VARCHAR(100) PRIMARY KEY,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    date VARCHAR(20),
    time VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


