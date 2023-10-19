-- first, import the database dump froma specified database to my server
-- This script then lists all shows contsined the the dump that have atleast one genre linekd
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
