-- hw4-queries.sql
set search_path to flight_database

-- 1. (20 points) List the names of carriers that operate flights from Seattle to San Francisco, CA.
-- Return each carrier's name only once. Use a nested query to answer this question.
-- Name the output column `carrier`. [Output relation cardinality: 4]

select distinct c.name as carrier
from carriers c
where c.cid in (select f.carrier_id
			   from flights f
			   where f.origin_city = 'Seattle WA'
			   and f.dest_city = 'San Francisco CA')


-- 2. (15 points) Express the same query as above but do so without using a nested query. Again, name the
-- output column `carrier`. [Output relation cardinality: 4]
			 
select distinct c.name as carrier
from flights f, carriers c
where f.origin_city = 'Seattle WA'
and f.dest_city = 'San Francisco CA'
and c.cid = f.carrier_id


-- 3. (15 points) List the weekdays (day_of_week in table weekdays) with at least 180000 flights per day. Use
-- a correlated nested query to answer this question. [Output relation cardinality: 3 rows]

select w.day_of_week
from weekdays w
where 180000 <= (select count(f.flight_num)
				 from flights f
				 where w.did = f.day_of_week_id)


-- 4. (15 points) Retrieve the carrier ids where the difference between the minimum and maximum flight
-- prices for that carrier is less than $900. Use a query in the FROM clause to answer this question.
-- [Output relation cardinality: 18]

select price_table.cid
from (select c.cid, min(f.price) as min_price, max(f.price) as max_price
	  from carriers c, flights f
	  where c.cid = f.carrier_id
	  group by c.cid) as price_table
where price_table.max_price - price_table.min_price < 900


-- 5. (15 points) Retrieve the carrier ids, the minimum and maximum flight prices where the difference
-- between the minimum and maximum flight prices for that carrier is less than $900. Do not use any nested
-- queries to answer this question. [Output relation cardinality: 18]

select c.cid, min(f.price), max(f.price)
from carriers c, flights f
where c.cid = f.carrier_id
group by c.cid
having max(f.price) - min(f.price) < 900


-- 6. (15 points) List the weekdays (day_of_week in table weekdays) where the difference between the
-- minimum and maximum flight prices for that day is less than $900. Use a correlated nested query to
-- answer this question. [Output relation cardinality: 3]

select w.day_of_week
from weekdays w
where w.did in (select f1.day_of_week_id
			  from flights f1
			  where w.did = f1.day_of_week_id
			  and 900 > (select max(f2.price) - min(f2.price)
						  from flights f2
						  where w.did = f2.day_of_week_id))


-- 7. (15 points) List the carrier names of all carriers that do not operate any flights.
-- [Output relation cardinality: 1571]

select distinct c.name
from carriers c
where c.cid not in (select f.carrier_id
					from flights f)

-- Using EXCEPT
select distinct c.name
from carriers c
except
select distinct c.name
from flights f, carriers c
where c.cid = f.carrier_id

-- 8. (10 points) Retrieve the flight ids of all flights operated by 'Hawaiian Airlines Inc.' and that fly on
-- Mondays. [Output relation cardinality: 1435]

select f.fid 
from flights f
where f.day_of_week_id = (select w.did
						  from weekdays w
						  where w.day_of_week = 'Monday')
and f.carrier_id = (select c.cid
					from carriers c
					where c.name = 'Hawaiian Airlines Inc.' )
					