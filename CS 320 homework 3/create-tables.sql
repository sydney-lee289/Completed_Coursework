-- create-tables.sql
create schema flight_database
set search_path to flight_database

create table Carriers(
	cid text primary key,
	name text);
	
create table Months(
	mid integer primary key,
	month text);
	
create table Weekdays(
	did integer primary key,
	day_of_week text);
	
create table Flights(
	fid integer primary key,
	month_id integer not null references Months(mid),
	day_of_month integer,
	day_of_week_id integer not null references Weekdays(did),
	carrier_id text not null references Carriers(cid),
	flight_num integer,
	origin_city text,
	origin_state text,
	dest_city text,
	dest_state text,
	departure_delay integer,
	taxi_out integer,
	arrival_delay integer,
	cancelled integer,
	actual_time integer,
	distance integer,
	capacity integer,
	price numeric);
	
select *
from Carriers

select *
from Months

select *
from Weekdays

select *
from Flights