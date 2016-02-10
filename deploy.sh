#bin/bash

cd wwwidmer
git merge origin/master

cp static/ ../

cd ../
python2.7 manage.py makemigrations
python2.7 manage.py migrate

../apache2/bin/restart