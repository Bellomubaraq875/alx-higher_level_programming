-- This script lists all genres from the database and displays the number of shows linked to each
SELECT g.name AS genre, COUNT(s.genre_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS s
ON g.id = s.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
