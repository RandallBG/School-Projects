USE ap;

INSERT INTO invoice_line_items
VALUES
	(115, 1, 160,180.23, "Hard drive"),
    (115, 2, 527, 254.35, "Exchange Server update");
    
SELECT * FROM invoice_line_items
	WHERE invoice_id = 115;