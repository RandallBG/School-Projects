-- SHOW VARIABLES 
-- WHERE VARIABLE_NAME = "event_scheduler";

-- SET GLOBAL event_scheduler = ON;



CREATE EVENT audit_test
	ON SCHEDULE EVERY 1 MINUTE 
    DO
		INSERT INTO invoices_audit
        VALUES(1,1, 1.00, "update", NOW());
    
