use ap;

SELECT avg(invoice_total) as average_invoice from invoices
WHERE MONTH(invoice_date) = "4" AND YEAR(invoice_date) = "2014";
