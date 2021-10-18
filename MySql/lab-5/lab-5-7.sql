SELECT vendor_name, COUNT(DISTINCT li.account_number) AS number_of_gl_accounts
FROM vendors v 
JOIN invoices i
USING (vendor_id)
JOIN invoice_line_items li
USING (invoice_id)
GROUP BY vendor_name
HAVING number_of_gl_accounts > 1
