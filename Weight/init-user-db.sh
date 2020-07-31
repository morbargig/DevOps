#!/bin/bash
set -e
echo setup "username $MYSQL_ROOT_PASSWORD" "dbname weight"

psql -v ON_ERROR_STOP=1 --username "$MYSQL_ROOT_PASSWORD" <<-EOSQL
    CREATE USER weight;
    CREATE DATABASE weight;
    GRANT ALL PRIVILEGES ON DATABASE weight TO weight;
EOSQL
