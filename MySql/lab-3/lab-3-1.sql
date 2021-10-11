use ap;

SELECT invoice_id, vendor_name, invoice_number, invoice_date, (invoice_total - payment_total - credit_total) as balance_due
FROM invoices i
INNER JOIN vendors v
USING (vendor_id) 
HAVING balance_due > 0 
ORDER BY vendor_name

