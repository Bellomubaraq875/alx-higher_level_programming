-- thus script lists all shows in the database without a genre linked
SELECT t.title, g.genre_id
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS g
ON g.show_id = t.id
WHERE g.genre_id IS NULL
ORDER BY t.title ASC, g.genre_id ASC;
