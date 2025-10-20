INSERT INTO admin (username, password) VALUES 
('admin1', 'password123'),
('manager', 'manager2025');

INSERT INTO labour (name, gender, age, contact, address, skill, join_date) VALUES
('John Doe', 'Male', 30, '9876543210', '123 Main St', 'Electrician', '2025-01-15'),
('Alice Smith', 'Female', 25, '9123456780', '456 Elm St', 'Plumber', '2025-02-20'),
('Bob Johnson', 'Male', 28, '9988776655', '789 Pine St', 'Carpenter', '2025-03-10');

INSERT INTO project (name, location, start_date, end_date, status) VALUES
('City Mall Renovation', 'Downtown', '2025-04-01', '2025-07-01', 'Ongoing'),
('Office Building Construction', 'Uptown', '2025-05-15', '2025-12-01', 'Ongoing'),
('Bridge Repair', 'River Side', '2025-06-01', '2025-09-30', 'Ongoing');

INSERT INTO assignment (labour_id, project_id, assigned_date) VALUES
(1, 1, '2025-04-05'),
(2, 2, '2025-05-20'),
(3, 3, '2025-06-05'),
(1, 2, '2025-06-10');

INSERT INTO attendance (labour_id, date, status) VALUES
(1, '2025-10-01', 'Present'),
(2, '2025-10-01', 'Absent'),
(3, '2025-10-01', 'Present'),
(1, '2025-10-02', 'Present'),
(2, '2025-10-02', 'Present');

INSERT INTO wages (labour_id, amount, payment_date) VALUES
(1, 2000.50, '2025-10-05'),
(2, 1800.00, '2025-10-05'),
(3, 2100.75, '2025-10-05'),
(1, 2000.50, '2025-10-15');

