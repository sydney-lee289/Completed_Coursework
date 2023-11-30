-- hw3-queries.sql

set search_path to flight_database

-- 1. (15 points) List the distinct flight numbers of all flights from Seattle to Boston by Alaska Airlines Inc. on
-- Mondays. Also notice that, in the database, the city names include the state. So, Seattle appears as
-- Seattle WA. Name the output column `flight_num`.[Output relation cardinality: 3 rows]

select distinct f.flight_num
from weekdays w, flights f join carriers c
on c.cid = f.carrier_id
where c.name = 'Alaska Airlines Inc.'
and w.day_of_week = 'Monday'
and f.origin_city = 'Seattle WA'
and f.dest_city = 'Boston MA'


-- 2. (15 points) Find the day of the week with the longest average arrival delay. Return the name of the day
-- and the average delay.Name the output columns `day_of_week` and `delay`, in that order. 
-- (Hint: consider using `LIMIT`)[Output relation cardinality: 1 row]

select distinct w.day_of_week, avg(f.arrival_delay) as delay
from weekdays w, flights f
where f.day_of_week_id = w.did
group by w.day_of_week
order by avg(f.arrival_delay) desc
limit 1                                


-- 3. (15 points) Find the names of all airlines that ever flew more than 1000 flights in one day 
-- (i.e., a specific day/month, but not any 24-hour period). Return only the names of the airlines. 
-- Do not return any duplicates, i.e., airlines with the exact same name(use DISTINCT). 
-- Name the output column `name`.Hint: you can group by more than one column.[Output relation cardinality: 12 rows]

select distinct c.name, f.day_of_month
from carriers c, flights f
where c.cid = f.carrier_id
and f.flight_num > 1000 
group by c.name, f.day_of_month

select distinct c1.name
from carriers c1, flights f1
where c1.cid = f1.carrier_id
and f1.flight_num > 1000
group by c1.name

-- 4. (15 points) Find the maximum price of tickets between Seattle and New York, NY, for each airline
-- separately. Name the output columns `carrier` and `max_price`, in that order. [Output relation cardinality: 3 rows]

select c.name, max(f.price)
from carriers c, flights f
where c.cid = f.carrier_id
and f.origin_city = 'Seattle WA'
and f.dest_city = 'New York NY'
group by c.name


-- 5. (15 points) Find the total capacity of all direct flights that fly between Seattle and San Francisco, CA 
-- on July 10th. Name the output column `capacity`. [Output relation cardinality: 1 row]

select sum(f.capacity) as capacity
from flights f
where f.month_id = 7
and f.day_of_month = 10
and f.origin_city = 'Seattle WA'
and f.dest_city = 'San Francisco CA'   


-- 6. Bonus! (10 points) Compute the total departure delay of each airline across all flights.
-- Name the output columns `name` and `delay`, in that order. [Output relation cardinality: 22 rows]

select c.name, sum(f.departure_delay) as delay
from carriers c, flights f
where c.cid = f.carrier_id
group by c.name                          


