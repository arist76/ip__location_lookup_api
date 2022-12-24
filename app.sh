#!/bin/bash
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

echo "\copy ip_lookup_ipv4model FROM ./data/IPV4.CSV DELIMITER ',' CSV;" | \
PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h db -p 5432 -d $POSTGRES_DB
echo "\copy ip_lookup_ipv6model FROM ./data/IPV6.CSV DELIMITER ',' CSV;" | \
PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h db -p 5432 -d $POSTGRES_DB

uwsgi --ini uwsgi_config.ini