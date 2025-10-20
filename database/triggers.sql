-- ========================
-- TRIGGERS
-- ========================

-- Set default join_date for new labour
DELIMITER $$
CREATE TRIGGER default_join_date
BEFORE INSERT ON labour
FOR EACH ROW
BEGIN
    IF NEW.join_date IS NULL THEN
        SET NEW.join_date = CURDATE();
    END IF;
END$$
DELIMITER ;

-- Set default assigned_date for new assignment
DELIMITER $$
CREATE TRIGGER default_assigned_date
BEFORE INSERT ON assignment
FOR EACH ROW
BEGIN
    IF NEW.assigned_date IS NULL THEN
        SET NEW.assigned_date = CURDATE();
    END IF;
END$$
DELIMITER ;

-- Set default payment_date for wages
DELIMITER $$
CREATE TRIGGER default_payment_date
BEFORE INSERT ON wages
FOR EACH ROW
BEGIN
    IF NEW.payment_date IS NULL THEN
        SET NEW.payment_date = CURDATE();
    END IF;
END$$
DELIMITER ;

-- Automatically mark project as complete if end_date is today or earlier
DELIMITER $$
CREATE TRIGGER project_complete_status
BEFORE UPDATE ON project
FOR EACH ROW
BEGIN
    IF NEW.end_date IS NOT NULL AND NEW.end_date <= CURDATE() THEN
        SET NEW.status = 'Complete';
    END IF;
END$$
DELIMITER ;
