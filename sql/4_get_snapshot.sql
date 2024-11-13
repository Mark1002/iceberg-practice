SELECT * FROM TABLE(table_history('nessie.people'))
order by made_current_at DESC;