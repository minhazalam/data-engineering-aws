-- create database for data modeling
create database data_model;
--use data_model;
create table data_model.customer_transactions(
    customer_id int,
    store_id int,
    spent float
);

create table customers(
    customer_id int,
    customer_name varchar,
    is_reward varchar
);

create table items_purchased(
    customer_id int,
    item_number int,
    item_name varchar
);

create table stores(
    store_id int,
    state varchar
);

-- insert into fact table customer_transactions
insert into customer_transactions(customer_id, store_id, spent)
values(1,1,20.50),
(2,1,35.21);

select * from customer_transactions;

delete from customer_transactions where customer_id=1;

insert into items_purchased(customer_id, item_number, item_name)
values (1, 1, 'Rubber Soul'),
       (2,3,'Let It Be');

insert into stores(store_id, state) VALUES (1,'CA'),(2,'WA');

insert into customers(customer_id, customer_name, is_reward) values (1,'Amanda','Y'),
(2, 'Toby','N');

-- Query 1: Find all the customers that spent more than 30 dollars, who are they,
-- which store they bought it from, location of the store, what they bought and if they are a rewards member.
select c.customer_name,s.store_id,s.state,ip.item_name,c.is_reward
from customer_transactions
join customers c on customer_transactions.customer_id = c.customer_id
join items_purchased ip on c.customer_id = ip.customer_id
inner join stores s on customer_transactions.store_id = s.store_id
where spent>30;

-- Query 2: How much did Customer 2 spend?
select customer_id,spent
from customer_transactions
where customer_id=2;