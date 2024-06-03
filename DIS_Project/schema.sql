DROP TABLE IF EXISTS countries_health;
DROP TABLE IF EXISTS countries_gdp;
DROP TABLE IF EXISTS countries_continent;
DROP TABLE IF EXISTS countries_random;
DROP TABLE IF EXISTS countries_language;

DROP SCHEMA IF EXISTS public; 

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

CREATE TABLE IF NOT EXISTS countries_language(
	Country				varchar(60),
	Official_language	varchar(60)
);



COPY countries_health(Country, LifeExpectancy,FertilityRate,Population,Region) FROM %s WITH CSV HEADER DELIMITER ',';
COPY countries_gdp(year,rank,Country,state,gdp,gdp_percent) FROM %s WITH CSV HEADER DELIMITER ',';
COPY countries_continent(Continent,Country) FROM %s WITH CSV HEADER DELIMITER ',';
COPY countries_language(Country, Official_language) FROM %s WITH CSV HEADER DELIMITER ',';
