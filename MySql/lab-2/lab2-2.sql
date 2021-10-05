SELECT invoice_number, invoice_due_date, invoice_total,
	(invoice_total * .10) AS ten_percent, (invoice_total * 1.10) AS total_plus_ten_percent
    FROM invoices WHERE invoice_total BETWEEN 500 AND 1000
    ORDER BY invoice_due_date DESC