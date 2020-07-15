#!/bin/bash
set -e
echo setup "username $POSTGRES_USER" "dbname $POSTGRES_DB"

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE USER gutendex;
    CREATE DATABASE gutendex;
    GRANT ALL PRIVILEGES ON DATABASE gutendex TO gutendex;
EOSQL
