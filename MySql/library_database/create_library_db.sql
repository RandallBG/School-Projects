DROP DATABASE IF EXISTS library;

CREATE DATABASE library;

USE library;

CREATE TABLE users 
(
	user_id			INT PRIMARY KEY AUTO_INCREMENT,
    first_name		VARCHAR(50),
    last_name		VARCHAR(50),
    email			VARCHAR(200) UNIQUE,
    username		VARCHAR(30) UNIQUE,
	user_password	VARCHAR(200)
);


CREATE TABLE books 
(
	isbn		INT PRIMARY KEY,
    title		VARCHAR(100),
    author		VARCHAR(100),
    book_desc   VARCHAR(1000)
);

CREATE TABLE genre
(
	genre_id		INT PRIMARY KEY AUTO_INCREMENT,
    genre			VARCHAR(20) UNIQUE
);

CREATE TABLE book_genres
(
	isbn	INT REFERENCES books (isbn),
	genre_id	INT REFERENCES genre (genre_id)
);


CREATE TABLE checkout_records
(
	user_id		INT REFERENCES users (user_id),
    isbn		INT REFERENCES books (isbn),
    date_issued	DATE,
    due_date	DATE,
    return_date	DATE
);


-- FILL OUT SOME OF THE TABLES --
INSERT INTO users
VALUES 	(DEFAULT, "Guest", NULL, "GUEST@gmail.com", "Guest", "password"),
		(DEFAULT, "Randall", "Gosnell", "Randall.bg.gosnell@gmail.com", "JustRandall", "password");
        
INSERT INTO books 
VALUES  (0345391802, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "After Earth is demolished to make way for a new hyperspatial expressway, Arthur Dent begins to hitch-hike through space."),
		(0544003415, "The Lord of the Rings", "J.R.R. Tolkien", "In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell by chance into the hands of the hobbit Bilbo Baggins.");
        
INSERT INTO genre
VALUES (DEFAULT, "Fiction"),(DEFAULT, "Non-Fiction"),(DEFAULT, "Comedy"), (DEFAULT, "Horror"),(DEFAULT, "Fantasy"),(DEFAULT, "Science Fiction"), (DEFAULT, "Action"), (DEFAULT, "Mystery");

INSERT INTO book_genres
VALUE (0345391802, 3), ("0345391802", 6),(0544003415, 5), (0544003415, 2);


INSERT INTO checkout_records
VALUE (2, 0345391802, "2021/04/28", "2021/05/28", "2021/06/22"),
		(1, 0345391802, "2021/03/20", "2021/04/20", NULL);


		

