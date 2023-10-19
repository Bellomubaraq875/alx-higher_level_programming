-- This script uses the database to list all genres not linked to the show Dexter
SELECT g.name
FROM tv_genres AS g
WHERE g.name NOT IN (
	SELECT tv_genres.name
	FROM tv_genres
	INNER JOIN tv_show_genres AS s
	ON tv_genres.id = s.genre_id
	INNER JOIN tv_shows
	ON tv_shows.id = s.show_id
	WHERE tv_shows.title = "Dexter")
ORDER BY g.name ASC;
