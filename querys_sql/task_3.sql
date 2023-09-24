/*
3 - Escreva uma consulta SQL que retorne o nome dos atores que atuaram em pelo menos 15 filmes.
*/

select
	a.first_name,
	a.last_name,
	count(fa.film_id)
from actor a

join
	film_actor fa on a.actor_id = fa.actor_id

where (
	fa.film_id >= 15
)

group by (
	a.actor_id, a.first_name, a.last_name
)