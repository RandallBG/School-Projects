use ap;

SELECT vendor_name, SUM(payment_total) as payment_sum  from vendors
JOIN invoices
ON vendors.vendor_id = invoices.vendor_id
group by vendor_name
ORDER BY payment_sum desc