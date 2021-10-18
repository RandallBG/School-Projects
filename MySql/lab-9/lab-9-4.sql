
DROP TRIGGER IF EXISTS invoices_after_update;

DELIMITER //

CREATE TRIGGER invoices_after_update 
AFTER UPDATE ON invoices
FOR EACH ROW
BEGIN

INSERT INTO invoices_audit (vendor_id, invoice_number, invoices_total, action_type, action_date)
VALUES (OLD.vendor_id, OLD.invoice_number,  OLD.invoice_total, "update", NOW());

END//

DELIMITER ;