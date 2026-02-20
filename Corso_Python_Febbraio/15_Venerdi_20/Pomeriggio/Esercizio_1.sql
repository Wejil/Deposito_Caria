# use classicmodels
/*
select * from products where buyPrice > 50; */

# delete from orders where status = 'Cancelled' -- Errore 1175 - You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.

#set sql_safe_updates = 0; -- Togliere la "sicura"

#delete from orders where status = 'Cancelled'

#set sql_safe_updates = 1; -- per riattivare la "sicura"

-- Errore 1451: dati interconnessi.

select orderNumber 
from orders 
where status = 'Cancelled';

-- 1. Eliminiamo i dettagli dei prodotti riferiti agli ordini cancellati
delete from orderdetails 
where orderNumber IN (
    select orderNumber 
    from (select orderNumber from orders where status = 'Cancelled') as temp_table
);

-- 2. Eliminiamo gli ordini veri e propri dalla tabella principale
delete from orders 
where status = 'Cancelled' 
and orderNumber > 0;