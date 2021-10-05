use ap;

SELECT CONCAT(vendor_contact_first_name, ", ",  vendor_contact_last_name) as full_name
from vendors
WHERE vendor_contact_last_name < "d" OR vendor_contact_last_name LIKE "E%"
order by vendor_contact_last_name, vendor_contact_first_name;