SELECT vendor_name, COUNT(i.vendor_id) as invoice_number, SUM(i.invoice_total) as invoice_sum from vendors v
JOIN invoices i on i.vendor_id = v.vendor_id
group by vendor_name
order by invoice_number desc