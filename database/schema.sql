-- ========================
-- LABOUR MANAGEMENT SCHEMA
-- ========================

CREATE DATABASE labour_db;
USE labour_db;


CREATE TABLE IF NOT EXISTS labour (
    labour_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INTEGER,
    gender VARCHAR(50),
    contact TEXT,
    address TEXT,
    skill TEXT,
    join_date DATE
);


CREATE TABLE IF NOT EXISTS project (
    project_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(500) NOT NULL,
    location TEXT,
    start_date DATE,
    end_date DATE,
    status VARCHAR(3000) DEFAULT 'Ongoing'
);


CREATE TABLE IF NOT EXISTS assignment (
    assignment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER,
    project_id INTEGER,
    assigned_date DATE,
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER,
    date DATE,
    status TEXT CHECK(status IN ('Present', 'Absent')),
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS wages (
    wage_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER,
    amount REAL,
    payment_date DATE,
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS admin (
    admin_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(16) NOT NULL
);
