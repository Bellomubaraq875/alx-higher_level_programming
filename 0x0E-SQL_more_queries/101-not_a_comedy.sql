-- This script lists all shows without the genre Comedy in the database
SELECT s.title
FROM tv_shows AS s
WHERE s.id NOT IN (
	SELECT tv_shows.id
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
	INNER JOIN tv_genres AS g
	ON tv_show_genres.genre_id = g.id
	WHERE g.name = "Comedy")
ORDER BY s.title ASC;
