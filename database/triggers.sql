-- ========================
-- TRIGGERS
-- ========================

DELIMITER $$

-- Automatically set project status to 'Complete' if end_date <= current date
CREATE TRIGGER trg_project_status_complete
BEFORE INSERT ON project
FOR EACH ROW
BEGIN
    -- If end_date is present and already passed, mark as Complete
    IF NEW.end_date IS NOT NULL AND NEW.end_date <= CURDATE() THEN
        SET NEW.status = 'Complete';
    
    -- If no end_date or a future one, mark as Ongoing
    ELSEIF NEW.status IS NULL OR NEW.status = '' THEN
        SET NEW.status = 'Ongoing';
    END IF;
END$$


-- Automatically set join_date if missing
CREATE TRIGGER trg_labour_join_date
BEFORE INSERT ON labour
FOR EACH ROW
BEGIN
    IF NEW.join_date IS NULL THEN
        SET NEW.join_date = CURDATE();
    END IF;
END$$

-- Automatically set assigned_date if missing
CREATE TRIGGER trg_assignment_date
BEFORE INSERT ON assignment
FOR EACH ROW
BEGIN
    IF NEW.assigned_date IS NULL THEN
        SET NEW.assigned_date = CURDATE();
    END IF;
END$$

-- Automatically set payment_date if missing
CREATE TRIGGER trg_wages_payment_date
BEFORE INSERT ON wages
FOR EACH ROW
BEGIN
    IF NEW.payment_date IS NULL THEN
        SET NEW.payment_date = CURDATE();
    END IF;
END$$

DELIMITER ;