SELECT * FROM ap.invoice_line_items;

SELECT gla.account_description,  SUM(ili.line_item_amount) AS invoice_sum FROM general_ledger_accounts gla
JOIN invoice_line_items ili
USING(account_number)
GROUP BY ili.account_number 
WITH ROLLUP
ORDER BY invoice_sum 
