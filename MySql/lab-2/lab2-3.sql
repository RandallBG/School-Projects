use ap;
SELECT invoice_number, invoice_total, (payment_total + credit_total) AS payment_credit_total,
(invoice_total - payment_total - credit_total) AS balance_due
	FROM invoices 
    HAVING balance_due > 50
    ORDER BY balance_due desc