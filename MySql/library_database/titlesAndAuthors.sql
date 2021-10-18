
SELECT atb.isbn, b.title, a.author_name  FROM authors_to_books atb
JOIN authors a
using (author_id)
JOIN books b
using (isbn)


