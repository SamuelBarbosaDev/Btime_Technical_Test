/*
1 - Escreva uma consulta SQL que retorne o nome e o sobrenome de todos os clientes que 
alugaram filmes no mês de agosto de 2022:
*/

select
    c.first_name,
    c.last_name
from customer c

join
    rental r on c.customer_id = r.customer_id

where(
    TO_CHAR(r.rental_date, 'YYYY-MM') = '2022-08'
)