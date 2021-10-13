USE ap;

SELECT vendor_id, SUM(invoice_total) as invoice_totals from invoices
GROUP BY vendor_id