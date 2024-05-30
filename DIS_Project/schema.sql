CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS countries_health(
	Country 				varchar(60),
	LifeExpectancy			float,
	FertilityRate			float,
	Population				bigint,
	Region					varchar(60)
);
CREATE TABLE IF NOT EXISTS countries_gdp(
	year 				int,
	rank				int,
	Country				varchar(60),
	state				varchar(60),
	gdp					bigint,
	gdp_percent			float
);

CREATE TABLE IF NOT EXISTS countries_continent(
	Continent			varchar(20),
	Country				varchar(60)
);

CREATE TABLE IF NOT EXISTS countries_random(
	Country				varchar(60),
	Co2_Emissions		varchar(60),
	Official_language	varchar(60)
);


