use ap;



-- SELECT invoice_due_date, payment_date, DATEDIFF(payment_date, invoice_due_date) as Days_Late FROM invoices
-- 	having Days_Late > 0
--     order by Days_Late DESC

SELECT vendor_id, vendor_name FROM invoices i join
