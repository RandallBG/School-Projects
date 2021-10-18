USE ap;
DROP PROCEDURE IF EXISTS test;

-- Change statement delimiter from semicolon to double front slash
DELIMITER //

CREATE PROCEDURE test()
    BEGIN
    DECLARE invoice_count_var int;
    SELECT COUNT(*)
    INTO invoice_count_var
    FROM invoices
    WHERE invoice_total - payment_total - credit_total >= 5000;

    
	SELECT CONCAT('Number greater than 5000 : ', invoice_count_var ) AS message;
END//

-- Change statement delimiter from double front slash to semicolon
DELIMITER ;
CALL test();  