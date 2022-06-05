SELECT * FROM information_schema.VIEWS v 
WHERE TABLE_SCHEMA  != 'sys'


DROP VIEW customers ;
DROP VIEW stg_customers ;
DROP VIEW stg_orders ;