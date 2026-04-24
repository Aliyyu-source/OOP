-- ============================================================
-- 1. BOOKS AND AUTHORS
-- ============================================================

CREATE TABLE authors (
    author_id   INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    nationality VARCHAR(50)
);

CREATE TABLE books (
    book_id     INT PRIMARY KEY,
    title       VARCHAR(200) NOT NULL,
    genre       VARCHAR(50),
    published   INT,
    author_id   INT REFERENCES authors(author_id)
);

INSERT INTO authors VALUES
    (1, 'Tove Jansson',       'Finnish'),
    (2, 'Fyodor Dostoevsky',  'Russian'),
    (3, 'Chimamanda Adichie', 'Nigerian');

INSERT INTO books VALUES
    (1, 'The Moomins and the Great Flood', 'Fantasy',  1945, 1),
    (2, 'Finn Family Moomintroll',         'Fantasy',  1948, 1),
    (3, 'Crime and Punishment',            'Classic',  1866, 2),
    (4, 'Half of a Yellow Sun',            'Literary', 2006, 3);

-- List all books with their author and nationality, ordered by publication year
SELECT
    b.title,
    b.genre,
    b.published,
    a.name        AS author,
    a.nationality
FROM books b
JOIN authors a ON b.author_id = a.author_id
ORDER BY b.published;
