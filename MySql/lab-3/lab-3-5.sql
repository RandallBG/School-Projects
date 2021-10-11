USE ap;

SELECT vendor_name, "CA" AS vendor_state
FROM vendors 
WHERE vendor_state = "CA"
UNION 
SELECT vendor_name, "Outside CA" AS vendor_state
FROM vendors
WHERE vendor_state != "CA"
ORDER BY vendor_name
