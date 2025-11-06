-- =======================
-- LABOUR MANAGEMENT SYSTEM (VALIDATED SCHEMA)
-- ========================

CREATE DATABASE IF NOT EXISTS labour_db;
USE labour_db;

-- =========================================
-- TABLE: labour
-- =========================================
CREATE TABLE IF NOT EXISTS labour (
    labour_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INTEGER CHECK (age BETWEEN 18 AND 65),
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    contact VARCHAR(15) CHECK (contact REGEXP '^[0-9]{10,15}$'),
    address VARCHAR(255),
    skill ENUM('Mason', 'Carpenter', 'Electrician', 'Plumber', 'Painter', 'Helper', 'Other') DEFAULT 'Other',
    join_date DATE DEFAULT (CURDATE())
);

-- =========================================
-- TABLE: project
-- =========================================
CREATE TABLE IF NOT EXISTS project (
    project_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    location VARCHAR(255) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NULL,
    status ENUM('Ongoing', 'On Hold', 'Complete', 'Cancelled') DEFAULT 'Ongoing',
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- =========================================
-- TABLE: assignment
-- =========================================
CREATE TABLE IF NOT EXISTS assignment (
    assignment_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    assigned_date DATE DEFAULT (CURDATE()),
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES project(project_id) ON DELETE CASCADE
);

-- =========================================
-- TABLE: attendance
-- =========================================
CREATE TABLE IF NOT EXISTS attendance (
    attendance_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER NOT NULL,
    date DATE NOT NULL DEFAULT (CURDATE()),
    status ENUM('Present', 'Absent', 'Leave') DEFAULT 'Absent',
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE,
    UNIQUE (labour_id, date) -- prevent duplicate entries
);

-- =========================================
-- TABLE: wages
-- =========================================
CREATE TABLE IF NOT EXISTS wages (
    wage_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    labour_id INTEGER NOT NULL,
    amount DECIMAL(10,2) CHECK (amount > 0) DEFAULT 500,
    payment_date DATE DEFAULT (CURDATE()),
    FOREIGN KEY (labour_id) REFERENCES labour(labour_id) ON DELETE CASCADE
);

-- =========================================
-- TABLE: admin
-- =========================================
CREATE TABLE IF NOT EXISTS admin (
    admin_id INTEGER PRIMARY KEY AUTO_INCREMENT,

    username VARCHAR(100) UNIQUE NOT NULL
        CHECK (
            LENGTH(username) BETWEEN 4 AND 16
            AND username REGEXP '^[A-Za-z0-9_]+$'
        ),

    password VARCHAR(100) NOT NULL
        CHECK (
            LENGTH(password) BETWEEN 8 AND 20
            AND password REGEXP '^(?=.*[A-Za-z])(?=.*[0-9]).{8,20}$'
        )
);