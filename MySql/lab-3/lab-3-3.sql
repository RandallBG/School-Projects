use ap;

SELECT vendor_name, invoice_date, invoice_number, invoice_sequence, line_item_amount
FROM vendors v
JOIN invoices i USING (vendor_id)
JOIN invoice_line_items ILI 
USING (invoice_id)
ORDER BY vendor_name, invoice_date, invoice_number, invoice_sequence;

