use ap;

SELECT avg(DATEDIFF(payment_date, invoice_date)) as average_days_to_pay from invoices
WHERE MONTH(invoice_date) = 5 AND YEAR(invoice_date) = "2014"
