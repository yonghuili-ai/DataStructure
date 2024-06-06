  /*

 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
       # sales                                # products
       +------------------+---------+         +---------------------+---------+
       | product_id       | INTEGER |>--------| product_id          | INTEGER |
       | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
       | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
  +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
  |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
  |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
  |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
  |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
  |    +------------------+---------+    |    +---------------------+---------+
  |                                      |
  |    # promotions                      |    # product_classes
  |    +------------------+---------+    |    +---------------------+---------+
  +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
       | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
       | media_type       | VARCHAR |         | product_category    | VARCHAR |
       | cost             | DECIMAL |         | product_department  | VARCHAR |
       | start_date       | DATE    |         | product_family      | VARCHAR |
       | end_date         | DATE    |         +---------------------+---------+
       +------------------+---------+

 */ 
 /*
 PROMPT:
 -- What percent of all products in the grocery chain's catalog
 -- are both low fat and recyclable?
 

 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------------------+
 | pct_low_fat_and_recyclable |
 +----------------------------+
 |         15.384615384615385 |
 +----------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ---------------- 
 */

select sum(case when is_low_fat_flg = 1 and is_recyclable_flg = 1 then 1 else 0 end)*100.0/count(1) as pct_low_fat_and_recyclable
from products








 /*
 BACKGROUND:

 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 The relationship between the four tables we want to analyze is depicted below:

       # sales                                # products
       +------------------+---------+         +---------------------+---------+
       | product_id       | INTEGER |>--------| product_id          | INTEGER |
       | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
       | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
  +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
  |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
  |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
  |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
  |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
  |    +------------------+---------+    |    +---------------------+---------+
  |                                      |
  |    # promotions                      |    # product_classes
  |    +------------------+---------+    |    +---------------------+---------+
  +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
       | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
       | media_type       | VARCHAR |         | product_category    | VARCHAR |
       | cost             | DECIMAL |         | product_department  | VARCHAR |
       | start_date       | DATE    |         | product_family      | VARCHAR |
       | end_date         | DATE    |         +---------------------+---------+
       +------------------+---------+
 */
 /*
 PROMPT:
 -- What are the top five (ranked in decreasing order)
 -- single-channel media types that correspond to the most money
 -- the grocery chain had spent on its promotional campaigns?

 Single Media Channel Types are promotions that contain only one media type.

 EXPECTED OUPTUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +---------------------------+------------+
 | single_channel_media_type | total_cost |
 +---------------------------+------------+
 | In-Store Coupon           | 70800.0000 |
 | Street Handout            | 70627.0000 |
 | Radio                     | 60192.0000 |
 | Sunday Paper              | 56994.0000 |
 | Product Attachment        | 50815.0000 |
 +---------------------------+------------+
 
-------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

select media_type as single_channel_media_type, sum(cost) as total_cost
from promotions
where media_type not like '%,%'
group by 1 
order by sum(cost) desc 
limit 5

 









 
 
 
 /*
 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT:
 -- Of sales that had a valid promotion, the VP of marketing
 -- wants to know what % of transactions occur on either
 -- the very first day or the very last day of a promotion campaign.
 
 
 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-------------------------------------------------------------+
 | pct_of_transactions_on_first_or_last_day_of_valid_promotion |
 +-------------------------------------------------------------+
 |                                         41.9047619047619048 |
 +-------------------------------------------------------------+
  
 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */

select sum(case when transaction_date = start_date then 1 when transaction_date=end_date then 1 else 0 end)*100.00/
sum(case when transaction_date between start_date and end_date then 1 else 0 end) as pct_of_transactions_on_first_or_last_day_of_valid_promotion
from 
(select s.transaction_date, p.start_date, p.end_date 
from sales as s 
left join promotions  as p 
on s.promotion_id = p.promotion_id) as tmp 

 /*
 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT
 -- The CMO is interested in understanding how the sales of different
 -- product families are affected by promotional campaigns.
 -- To do so, for each of the available product families,
 -- show the total number of units sold,
 -- as well as the ratio of units sold that had a valid promotion
 -- to units sold without a promotion,
 -- ordered by increasing order of total units sold.
 
 
 EXPECTED OUTPUT
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------+------------------+--------------------------------------------------+
 | product_family | total_units_sold | ratio_units_sold_with_promo_to_sold_without_promo|
 +----------------+------------------+--------------------------------------------------+
 | Drink          |          43.0000 |                           0.79166666666666666667 |
 | Non-Consumable |         176.0000 |                           0.76000000000000000000 |
 | Food           |         564.0000 |                           0.75155279503105590062 |
 +----------------+------------------+--------------------------------------------------+
 
 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */
 





/*
 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT:
 -- The VP of Sales feels that some product categories don't sell
 -- and can be completely removed from the inventory.
 -- As a first pass analysis, they want you to find what percentage
 -- of product categories have never been sold.
 
 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-----------------------------------+
 | pct_product_categories_never_sold |
 +-----------------------------------+
 |               13.8888888888888889 |
 +-----------------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 */















/**

BACKGROUND:

The following schema is that of a relational database of a grocery store
chain. This chain sells many products in its multiple stores across many 
states to its many customers. The relationship between all four tables is 
depicted below:    

products                              sales
+------------------+---------+        +------------------+---------+
| product_id       | int     |------->| product_id       | int     |
| product_class_id | int     |  +---->| store_id         | int     |
| brand_name       | varchar |  |  +->| customer_id      | int     |
| product_name     | varchar |  |  |  | promotion_id     | int     |
| price            | int     |  |  |  | store_sales      | decimal |
+------------------+---------+  |  |  | store_cost       | decimal |
                                |  |  | units_sold       | decimal |
                                |  |  | transaction_date | date    |
                                |  |  +------------------+---------+
                                |  | 
stores                          |  |  customers
+-------------------+---------+ |  |  +---------------------+---------+
| store_id          | int     |-+  +--| customer_id         | int     |
| type              | varchar |       | first_name          | varchar |
| name              | varchar |       | last_name           | varchar |
| state             | varchar |       | state               | varchar |
| first_opened_date | datetime|       | birthdate           | date    |
| last_remodel_date | datetime|       | education           | varchar |
| area_sqft         | int     |       | gender              | varchar |
+-------------------+---------+       | date_account_opened | date    |
                                      +---------------------+---------+

What is the best selling product in each store? 
--Which metric is used to validate best selling?
Use the max units sold. 
-- What output is expected?
store_id, product_id, units_sold

with max_unit as
(
    select store_id, max(units_sold) as mx
    from sales
    group by 1
)
select s.store_id, s.product_id, s.units_sold
from sales as s
join max_unit as m
on m.store_id = s.store_id
where s.units_sold = m.mx

What is the gross profit percentage that we earned in each state where we have stores?

with store_in_state as
(
    select s.store_id, s.store_sales, s.store_cost, st.state
    from sales as s
    join stores as st
    on st.store_id = s.store_id
) select state, (sum(store_sales) - sum(store_cost))/ sum(store_cost * 100 as percentage
from store_in_state
group by 1

select store_id, (store_sales - store_cost)/store_cost * 100 as percentage
    from sales

**/
# ask 1 or 2 questions, what is the final output should look like?
# what is the definition of best selling, is that unit sold, or sales of product?

# write the query first, then explain your query. 

with best_selling_product as (
select store_id, max(store_sales) as max_store_sales as best_selling_product
from sales
group by store_id
),
product_id_best_selling as (
select product_id , store_sales, store_id
from sales s
join best_selling_product b
on s.store_id = b.store_id
where store_sales = max_store_sales
)


 /*
 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT
 -- The CMO is interested in understanding how the sales of different
 -- product families are affected by promotional campaigns.
 -- To do so, for each of the available product families,
 -- show the total number of units sold,
 -- as well as the ratio of units sold that had a valid promotion
 -- to units sold without a promotion,
 -- ordered by increasing order of total units sold.
 

 EXPECTED OUTPUT
 Note: Please use the column name(s) specified in the expected output in your solution.
 +----------------+------------------+--------------------------------------------------+
 | product_family | total_units_sold | ratio_units_sold_with_promo_to_sold_without_promo|
 +----------------+------------------+--------------------------------------------------+
 | Drink          |          43.0000 |                           0.79166666666666666667 |
 | Non-Consumable |         176.0000 |                           0.76000000000000000000 |
 | Food           |         564.0000 |                           0.75155279503105590062 |
 +----------------+------------------+--------------------------------------------------+
 
 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------
 --qeustions to ask: how to tell if unit sold is with promo?
 --answer: if promo_id <> 0
 */
 

 select product_family, 
 sum(units_sold)*1.00 as total_units_sold, 
 sum(case when promotion_id <> 0 then units_sold*1.0 else 0 end) / sum(case when promotion_id = 0 then units_sold*1.0 else 0 end)  as ratio_units_sold_with_promo_to_sold_without_prom
 from 
 (select s.promotion_id, s.units_sold, pc.product_family 
   from sales as s
   (left or)join products as p
   on p.product_id  = s.product_id 
   (left or )join product_classes as pc
   on p.product_class_id = pc.product_class_id
  )
 group by 1 
 order by total_units_sold



  /*
 BACKGROUND:
 
 The following schema is a subset of a relational database of a grocery store
 chain. This chain sells many products of different product classes to its
 customers across its different stores. It also conducts many different
 promotion campaigns.
 
 The relationship between the four tables we want to analyze is depicted below:
 
        # sales                                # products
        +------------------+---------+         +---------------------+---------+
        | product_id       | INTEGER |>--------| product_id          | INTEGER |
        | store_id         | INTEGER |    +---<| product_class_id    | INTEGER |
        | customer_id      | INTEGER |    |    | brand_name          | VARCHAR |
   +---<| promotion_id     | INTEGER |    |    | product_name        | VARCHAR |
   |    | store_sales      | DECIMAL |    |    | is_low_fat_flg      | TINYINT |
   |    | store_cost       | DECIMAL |    |    | is_recyclable_flg   | TINYINT |
   |    | units_sold       | DECIMAL |    |    | gross_weight        | DECIMAL |
   |    | transaction_date | DATE    |    |    | net_weight          | DECIMAL |
   |    +------------------+---------+    |    +---------------------+---------+
   |                                      |
   |    # promotions                      |    # product_classes
   |    +------------------+---------+    |    +---------------------+---------+
   +----| promotion_id     | INTEGER |    +----| product_class_id    | INTEGER |
        | promotion_name   | VARCHAR |         | product_subcategory | VARCHAR |
        | media_type       | VARCHAR |         | product_category    | VARCHAR |
        | cost             | DECIMAL |         | product_department  | VARCHAR |
        | start_date       | DATE    |         | product_family      | VARCHAR |
        | end_date         | DATE    |         +---------------------+---------+
        +------------------+---------+
 */
 /*
 PROMPT:
 -- The VP of Sales feels that some product categories don't sell
 -- and can be completely removed from the inventory.
 -- As a first pass analysis, they want you to find what percentage
 -- of product categories have never been sold.
 
 EXPECTED OUTPUT:
 Note: Please use the column name(s) specified in the expected output in your solution.
 +-----------------------------------+
 | pct_product_categories_never_sold |
 +-----------------------------------+
 |               13.8888888888888889 |
 +-----------------------------------+

 -------------- PLEASE WRITE YOUR SQL SOLUTION BELOW THIS LINE ----------------

 
 
 select * from sales*/
 
--how to define percentage of product categories have never been sold?
-- assume the persentage of distinct product count which can not found in sales table over total counts in products
select (select count(*) from products where product_id not in (select product_id from sales)) * 1.0/(select count(distinct product_id) from products) as pct_product_categories_never_sold



/*SELECT 100.0 * (1 - COUNT(DISTINCT product_category) / CAST((SELECT COUNT(DISTINCT product_category) FROM product_classes) AS FLOAT64)) AS pct_product_categories_never_sold
FROM sales s JOIN products p ON (s.product_id=p.product_id) JOIN product_classes pc ON (p.product_class_id=pc.product_class_id)*/








