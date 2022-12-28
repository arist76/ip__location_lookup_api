#!/bin/bash
python3 manage.py makemigrations --no-input
python3 manage.py migrate --no-input

IS_IPV4_POPULATED=$(python3 manage.py populated ipv4)
if ! $IS_IPV4_POPULATED; then
    echo "Downloading IPv4 file"
    FILEv4=/application_root/data/IPV4.CSV
    if [ -e "$FILEv4" ]; then
        echo "$FILEv4 Already exists. Proceeding..."
    else
        wget -t 5 -P /application_root/data/ --retry-connrefused https://www.dropbox.com/s/eq9xwajq0lgoz8o/IPV4.CSV
    fi

    echo "Copying file to Postgresql"
    echo "\copy ip_lookup_ipv4model FROM ./data/IPV4.CSV DELIMITER ',' CSV;" | \
    PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h db -p 5432 -d $POSTGRES_DB
else
    echo "The IPv4 table is already populated. Skipping download and copy"
fi



IS_IPV6_POPULATED=$(python3 manage.py populated ipv6)
if ! $IS_IPV6_POPULATED; then
    FILEv6=/application_root/data/IPV6.CSV
    echo "Downloading IPv6 file"
    if [ -e "$FILEv6" ]; then
        echo "$FILEv6 Already Exists. Proceeding..."
    else
        wget -t 5 -P /application_root/data/ --retry-connrefused https://www.dropbox.com/s/mcbx5hfwgq1bpvx/IPV6.CSV
    fi
    
    echo "Copying file to Postgresql"
    echo "\copy ip_lookup_ipv6model FROM ./data/IPV6.CSV DELIMITER ',' CSV;" | \
    PGPASSWORD=$POSTGRES_PASSWORD psql -U $POSTGRES_USER -h db -p 5432 -d $POSTGRES_DB
else
    echo "The IPv6 table is already populated. Skipping download and copy"
fi



uwsgi --ini uwsgi_config.ini
