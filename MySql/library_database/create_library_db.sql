DROP DATABASE IF EXISTS library;

CREATE DATABASE library;

USE library;

CREATE TABLE users 
(
	user_id			INT PRIMARY KEY AUTO_INCREMENT,
    first_name		VARCHAR(50) NOT NULL,
    last_name		VARCHAR(50) NOT NULL,
    email			VARCHAR(200) NOT NULL UNIQUE,
    username		VARCHAR(30) NOT NULL UNIQUE,
	user_password	VARCHAR(200) NOT NULL
);


CREATE TABLE books 
(
	isbn		BIGINT PRIMARY KEY,
    title		VARCHAR(100)  NOT NULL,
    book_type	VARCHAR(50)   NOT NULL,
    book_desc   VARCHAR(1000) NOT NULL,
    image_index INT      
	
);

CREATE TABLE genre
(
	genre_id		INT PRIMARY KEY AUTO_INCREMENT,
    genre			VARCHAR(20) NOT NULL UNIQUE
);

CREATE TABLE books_to_genres
(
	isbn	BIGINT REFERENCES books (isbn),
	genre_id	INT REFERENCES genre (genre_id)
);

CREATE TABLE authors
(
	author_id	INT	PRIMARY KEY auto_increment,
    author_name VARCHAR(100) NOT NULL
);

CREATE TABLE authors_to_books
(
    isbn	  BIGINT REFERENCES books (isbn),
    author_id INT REFERENCES authors (author_id)
);

CREATE TABLE checkout_records
(
	user_id		INT REFERENCES users (user_id),
    isbn		BIGINT REFERENCES books (isbn),
    date_issued	DATE NOT NULL,
    due_date	DATE NOT NULL,
    return_date	DATE 
);


-- FILL OUT SOME OF THE TABLES --
INSERT INTO users
VALUES 	(DEFAULT, "Guest", "Guest", "GUEST@gmail.com", "Guest", "password"),
		(DEFAULT, "Randall", "Gosnell", "RandallG@gmail.com", "RandallG", "password");
        
INSERT INTO books 
VALUES  (9780307291813, "The Hitchhiker's Guide to the Galaxy", "paperback", "After Earth is demolished to make way for a new hyperspatial expressway, Arthur Dent begins to hitch-hike through space.",1),
		(9780547928210, "The Lord of the Rings","paperback", "In ancient times the Rings of Power were crafted by the Elven-smiths, and Sauron, the Dark Lord, forged the One Ring, filling it with his own power so that he could rule all others. But the One Ring was taken from him, and though he sought it throughout Middle-earth, it remained lost to him. After many ages it fell by chance into the hands of the hobbit Bilbo Baggins.",2),
        (9781250832375, "The Eye of the World(The Wheel of Time Book One)", "paperback", "When she arrives in a small village in the Two Rivers, Moiraine discovers three young men, each of whom might be the long-awaited and reviled Chosen One, the Dragon Reborn. But she is not the only stranger new to the village, nor the only one searching. In a race against time and the agents of the Shadow, she must guide her charges through lands of myth and legend. toward allies both new and old, and into the footsteps of prophecy.",3),
        (9780553381689, 'A Game of Thrones (Song of Ice and Fire)', "paperback",
			'Winter is coming. Such is the stern motto of House Stark, the northernmost of the fiefdoms that owe allegiance to King Robert Baratheon in far-off King’s Landing. There Eddard Stark of Winterfell rules in Robert’s name. There his family dwells in peace and comfort: his proud wife, Catelyn; his sons Robb, Brandon, and Rickon; his daughters Sansa and Arya; and his bastard son, Jon Snow. Far to the north, behind the towering Wall, lie savage Wildings and worse—unnatural things relegated to myth during the centuries-long summer, but proving all too real and all too deadly in the turning of the season.',4);
	
INSERT INTO authors
VALUES (default, "Douglas Adams"), (default, "J.R.R. Tolkien" ), (default, "Robert Jordan"), (default, "George R.R. Martin");

INSERT INTO authors_to_books
VALUES ("9780307291813", 1), ("9780547928210", 2), ("9781250832375", 3), ("9780553381689", 4);

INSERT INTO genre
VALUES (DEFAULT, "Fiction"),(DEFAULT, "Non-Fiction"),(DEFAULT, "Comedy"), (DEFAULT, "Horror"),(DEFAULT, "Fantasy"),(DEFAULT, "Science Fiction"), (DEFAULT, "Action"), (DEFAULT, "Mystery");

INSERT INTO books_to_genres
VALUE (0345391802, 3), (0345391802, 6),(0544003415, 5), (0544003415, 1), (9781250832375, 1), (9781250832375, 5), (978055310354, 1), (978055310354, 5);


INSERT INTO checkout_records
VALUE (2, 0345391802, "2021/04/28", "2021/05/28", "2021/06/22"),
		(1, 0345391802, "2021/03/20", "2021/04/20", NULL);


		

