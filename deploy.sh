#bin/bash
# CUSTOM

cd wwwidmer
git merge origin/master

cd ../
./manage.py makemigrations
./manage.py migrate

../apache2/bin/restart