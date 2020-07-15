#!/bin/bash
python3 /project/manage.py migrate
python3 /project/manage.py updatecatalog
echo yes | python3 manage.py collectstatic
/usr/bin/firefox 0.0.0.0:8000
# echo ""
python3 /project/manage.py runserver 0.0.0.0:8000