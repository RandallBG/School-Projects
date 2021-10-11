use ap;

SELECT vendor_name, default_account_number AS "Default Account", account_description AS "Description" 
FROM vendors v JOIN general_ledger_accounts GLA
 ON  v.default_account_number = GLA.account_number

