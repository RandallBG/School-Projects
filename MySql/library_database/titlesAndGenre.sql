SELECT title, g.genre FROM books
JOIN books_to_genres
USING (isbn)
JOIN genre g
USING (genre_id);
