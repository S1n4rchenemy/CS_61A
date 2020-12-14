.read data.sql


CREATE TABLE average_prices AS
  SELECT category AS category, SUM(MSRP) / COUNT(*) AS average_price FROM products
  GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT store, item, MIN(price) FROM inventory
  GROUP BY item;


CREATE TABLE price_per_rate AS
  SELECT name, category, MIN(MSRP / rating) AS price_rate FROM products
  GROUP BY category; 

CREATE TABLE shopping_list AS
  SELECT a.name AS item, b.store AS store FROM price_per_rate AS a, lowest_prices AS b
  WHERE a.name = b.item;


CREATE TABLE total_bandwidth AS
  SELECT SUM(a.Mbs) FROM stores AS a, shopping_list AS b
  WHERE a.store = b.store;

