CREATE SCHEMA iceberg.schema2 WITH (location = 's3://datalakehouse/schema2');

CREATE TABLE iceberg.schema2.users
(
  id INTEGER,
  name VARCHAR,
  height decimal(10,2),
  weight decimal(10,2),
)
WITH (
  format = 'PARQUET'
);

INSERT INTO iceberg.schema2.users
(id, name, height, weight) VALUES
(1, 'Tony', 178.5, 67),
(2, 'Sam', 180, 80)