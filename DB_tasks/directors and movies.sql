-- ============================================================
-- 5. DIRECTORS AND MOVIES
-- ============================================================

CREATE TABLE directors (
    director_id INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    birth_year  INT,
    country     VARCHAR(60)
);

CREATE TABLE movies (
    movie_id     INT PRIMARY KEY,
    title        VARCHAR(200) NOT NULL,
    release_year INT,
    genre        VARCHAR(50),
    imdb_score   NUMERIC(3, 1),
    director_id  INT REFERENCES directors(director_id)
);

INSERT INTO directors VALUES
    (1, 'Aki Kaurismäki',    1957, 'Finland'),
    (2, 'Christopher Nolan', 1970, 'UK'),
    (3, 'Bong Joon-ho',      1969, 'South Korea');

INSERT INTO movies VALUES
    (1, 'The Man Without a Past', 2002, 'Drama',    7.8, 1),
    (2, 'Le Havre',               2011, 'Drama',    7.5, 1),
    (3, 'Inception',              2010, 'Sci-Fi',   8.8, 2),
    (4, 'The Dark Knight',        2008, 'Action',   9.0, 2),
    (5, 'Parasite',               2019, 'Thriller', 8.5, 3);

-- List all movies with director details, ranked by IMDb score
SELECT
    d.name        AS director,
    d.country,
    m.title,
    m.release_year,
    m.genre,
    m.imdb_score
FROM movies m
JOIN directors d ON m.director_id = d.director_id
ORDER BY m.imdb_score DESC;
