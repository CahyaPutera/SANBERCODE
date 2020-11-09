
with cte1 as (
select albums.Title as 'Title', artists.Name as 'Name', tracks.Name as 'tracks'
from albums 
join artists on albums.ArtistId = artists.ArtistId
join tracks on albums.AlbumId = tracks.AlbumId
), cte2 as (
select * from cte1 
where Name = 'AC/DC' and Title = 'Let There Be Rock'
), cte3 as (
select * from cte1 where Name = 'Aerosmith'
) 
select * from cte2 
union all
select * from cte3;