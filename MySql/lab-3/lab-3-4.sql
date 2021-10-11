USE ap;



SELECT GLA.account_number, account_description, invoice_id
FROM general_ledger_accounts GLA
LEFT OUTER JOIN invoice_line_items ILI
ON GLA.account_number = ILI.account_number
WHERE ILI.invoice_id IS NULL
ORDER BY account_number



