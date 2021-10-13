use ap;

SELECT gla.account_description, COUNT(ili.line_item_amount) AS line_item_count, i.invoice_date,
SUM(ili.line_item_amount) AS line_item_sum  FROM general_ledger_accounts gla
inner JOIN invoices i 
JOIN invoice_line_items ili
WHERE gla.account_number = ili.account_number AND i.invoice_id	 = ili.invoice_id
GROUP BY account_description
HAVING i.invoice_date > "2014/4/1" AND i.invoice_date < "2014/6/20"




