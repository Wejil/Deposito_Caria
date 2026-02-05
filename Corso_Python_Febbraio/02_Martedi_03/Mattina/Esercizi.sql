select first_name as Nome
from actor;

select last_name as Cognome
from actor;

select title, rating
from film
where rating in ('G');

select *
from customer
where first_name like 'A%' and last_name like '%S';

select *
from film
where length>150 and rental_rate<1.00;

-- Mostra i 10 film più lunghi presenti nel database, ordinandoli dal più lungo al più corto.
select *
from film
order by length desc
limit 10;

-- Qual è il prezzo medio di noleggio (rental_rate) di tutti i film? Rinomina il risultato come "Prezzo_Medio_Noleggio".
select avg(rental_rate) as Prezzo_Medio_Noleggio
from film;

-- Nella tabella film, conta quanti film ci sono per ogni durata di noleggio (rental_duration).
select rental_duration, count(*)
from film
group by rental_duration;

-- Vai nella tabella payment e conta quanti pagamenti ha registrato ogni staff_id.
select staff_id, count(*)
from payment
group by staff_id;

-- Per ogni customer_id nella tabella payment, mostra il pagamento più alto (MAX) e quello più basso (MIN) che abbiano mai effettuato.
select customer_id, max(amount), min(amount)
from payment
group by customer_id;



