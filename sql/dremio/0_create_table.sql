CREATE TABLE nessie.schema1.people (
    id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    age INT
) 
PARTITION BY (truncate(1, last_name));