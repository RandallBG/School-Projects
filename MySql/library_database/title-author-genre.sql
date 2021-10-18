USE library;

SELECT isbn, title, author_name, genre from books bks
JOIN authors_to_books
	USING (isbn)
JOIN authors
	USING (author_id)
JOIN books_to_genres
	USING (isbn)
JOIN genre
	USING (genre_id)
ORDER BY title
