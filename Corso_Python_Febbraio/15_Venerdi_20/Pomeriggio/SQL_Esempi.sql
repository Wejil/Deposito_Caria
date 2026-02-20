-- create database prova; 2 trattini, commento standard.
-- drop database prova; per cancellare un database "drop".
#use prova; cancelletto usabile grazie a MySQL Workbench

/* create table utente (
id int primary key,
nome varchar(50)
) */ -- per commento multi riga si usa /* e */
/*
create table acquisti(
id int primary key,
tipo varchar(50),
idUtente int,
foreign key(idUtente) references utente(id)
) */
/*
create table acquistiCopia
select * from acquisti

use world; */
/*
create table city2
select * from city;

create table city3
select * from city; */
#drop table city3;

#truncate table city2;
/*
drop table city2;

create table city2
select * from city; */
/*
alter table city2
#add cap int; -- per aggiungere una colonna, mettere sempre l'int (intero)
#drop Population -- per cancellare una colonna
modify column ID int primary key -- per modificare una colonna */
/*
not null: no valori vuoti
unique: solo valori univoci
default: valore di default se valore vuoto inserito */
/*
select *
from city; -- seleziona tutti i valori della tabella city */
/*
select Name, Population
from city; -- selezionerà solo name e population (si possono scrivere anche in minuscolo, ma sempre meglio usare il maiuscolo) */
/*
select Distinct Population
from city;

select count(distinct Population)
from city; */
/*
select Name, Continent, Region
from country
where Continent = "Asia"; */

