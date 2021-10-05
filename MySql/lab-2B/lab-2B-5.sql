use ap;

SELECT invoice_number, invoice_due_date, payment_date,
	DATEDIFF(payment_date, invoice_due_date) as days_late from invoices
WHERE DATEDIFF(payment_date, invoice_due_date) > 0
