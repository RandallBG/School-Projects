use ap;

DROP VIEW IF EXISTS open_items;

CREATE VIEW open_items AS
SELECT v.vendor_name, i.invoice_number, i.invoice_total, (i.invoice_total - i.payment_total - i.credit_total) AS balance_due
FROM invoices i
JOIN vendors v
ON i.vendor_id = v.vendor_id
WHERE (i.invoice_total - i.payment_total - i.credit_total) > 0