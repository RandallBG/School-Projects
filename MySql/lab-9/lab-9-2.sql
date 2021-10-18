DELIMITER //

CREATE TRIGGER invoices_before_update
   BEFORE UPDATE ON invoices
   FOR EACH ROW
BEGIN
   DECLARE sum_line_item_amount_var DECIMAL(9,2);
   DECLARE payment_credit_sum_var DECIMAL (9,2);
   
   SELECT SUM(ili.line_item_amount), (i.payment_total + i.credit_total)
      INTO sum_line_item_amount_var, payment_credit_sum_var
   FROM invoice_line_items ili
   JOIN invoices i
   WHERE invoice_id = NEW.invoice_id;

   IF sum_line_item_amount_var != NEW.invoice_total
      THEN SIGNAL SQLSTATE 'HY000'
      SET MESSAGE_TEXT = 'Line item total must match invoice total.';
	END IF;
    
    IF payment_credit_sum_var > NEW.invoice_total
		THEN SIGNAL SQLSTATE "HY001"
        SET MESSAGE_TEXT = "credit and payment totals must not exceed invoice total";
	END IF;
		
END//

DELIMITER ;