cd /usr/local/mysql/bin/; ls
./mysql -u root -p


CREATE DATABASE shop;    - создаем базу данных shop (например)

\с shop   - коннектимся к ней
\d            - показывает какие таблицы уже есть в базе данных


CREATE TABLE customer(
    id serial primary key,
    name varchar(255),
    email varchar(50),
    phone varchar(50)
);

\d customer  - показывает описание таблицы customer (например)

CREATE TABLE product(
    id serial primary key,
    name varchar(255),
    description text,
    price integer);

CREATE TABLE product_photo(
    id serial primary key,
    url varchar(255),
    product_id integer references product(id));        - получается реляция (связь) сущностей таблиц FOREIGN KEY


CREATE TABLE cart(
    customer_id integer references customer(id),     - получается реляция (связь) сущностей таблиц FOREIGN KEY
    id serial primary key);


CREATE TABLE cart(                             - два поля в таблице ссылаются на внешние таблицы, образуя MANY TO MANY
    cart_id integer references cart(id),     
    product_id integer references product(id));


Добавляем данные в таблицу

insert into customer(name, phone, email) values('Василий', ‘102’, ‘vasya@gmail.com’);

Еще 

insert into customer(name, phone, email) values(‘Петр', ‘103’, ‘petr@gmail.com’);

select * from customer;                   - выбирает все записи в таблице customer

JOIN
Соединяет разные колонки из разных таблиц в одну таблицу

select * from product_photo pp;            - pp это алияс
select pp.* from product_photo pp; 
select pp.* from product_photo pp left join product p on p.id=pp.product_id;
select pp.*, p.name from product_photo pp left join product p on p.id=pp.product_id;

Мы соединили 2 таблицы в 1 финальную таблицу

\d product_photo
alter table product_photo from constraint product_photo_product_id_fkey;   - мы удалили FOREIGN KEY

insert into product_photo (‘url’, ‘product_id’) values (‘unknown/url’, 100);

select * from product_photo;             - в итоге мы видим как мы добавили фотографию

Удаление данных из таблиц

delete from product_photo where id=2;      - удаляет всю запись из таблицы по условию
update product_photo set url=‘iPhone_image_2’ where id=1;    - устанавливает новое значение по условию

Пример комплексного запроса с множеством JOIN

select c.name from customer c;
select c.name from customer c left join cart on cart.customer_id=c.id;    -  мы соединили таблицы customer и cart
select c.name, cart.id from customer c left join cart on cart.customer_id=c.id;

select c.name, cart.id as cart_id from customer c left join cart on cart.customer_id=c.id;

select c.name, cart.id as cart_id from customer c left join cart on cart.customer_id=c.id left join cart_product cp on cp.cart_id=cart.id;

select c.name, cart.id as cart_id, cp.product_id from customer c left join cart on cart.customer_id=c.id left join cart_product cp on cp.cart_id=cart.id;

select c.name, cart.id as cart_id, cp.product_id, p.price from customer c left join cart on cart.customer_id=c.id left join cart_product cp on cp.cart_id=cart.id left join product p on p.id=cp.product_id;

В итоге у нас получилась таблица которая состоит из имен клиентов, найди корзин (заказы это клиентов), найди продуктов (товаров) которые заказаны, цены на товар.

Группировка данных GROUP BY

select c.name, p.price from customer c left join cart on cart.customer_id=c.id left join cart_product cp on cp.cart_id=cart.id left join product p on p.id=cp.product_id;          - У нас получается таблица name и price.

select c.name, sum(p.price) from customer c left join cart on cart.customer_id=c.id left join cart_product cp on cp.cart_id=cart.id left join product p on p.id=cp.product_id group by c.name order by orders_sum desc;    - сортировка по сумме заказа

