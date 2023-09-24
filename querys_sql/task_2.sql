/*
2 - Escreva uma consulta SQL que calcule o total de receita (valor pago) para cada filme alugado.
*/

SELECT
    f.title AS film_title,
    SUM(p.amount) AS total_revenue
FROM
    rental r
JOIN
    payment p ON r.rental_id = p.rental_id
JOIN
    inventory i ON r.inventory_id = i.inventory_id
JOIN
    film f ON i.film_id = f.film_id
GROUP BY
    f.title
ORDER BY
    total_revenue DESC;