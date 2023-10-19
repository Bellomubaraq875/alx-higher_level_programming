-- This script lists all shows contained in a specified database on the command lline
SELECT t.title, g.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS g
ON g.show_id = t.id
ORDER BY t.title ASC, g.genre_id ASC;
