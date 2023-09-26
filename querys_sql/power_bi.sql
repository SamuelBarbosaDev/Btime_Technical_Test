/*
Query feita no Power BI.
*/
select
	f.title,
	ca.name as category,
	f.release_year,
	f.rental_duration,
	f.rental_rate,
	f.length,
	f.replacement_cost,
	pa.amount,
	r.rental_date,
	r.return_date,
	i.store_id,
	DATE_PART('day', r.return_date - r.rental_date) AS actual_rental_duration
from rental r

join payment pa on r.rental_id = pa.rental_id
join inventory i on r.inventory_id = i.inventory_id
join film f on i.film_id = f.film_id
join film_category fc on f.film_id = fc.film_id
join category ca on fc.category_id = ca.category_id
