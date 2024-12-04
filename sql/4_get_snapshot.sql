SELECT * FROM TABLE(table_history('nessie.schema1.people'))
order by made_current_at DESC;