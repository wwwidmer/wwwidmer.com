#bin/bash

# TODO CHECK WERE IN THE RIGHT DIRECTORY
# if not cd wwwidmer			
git merge origin/master

rm -r ../static/
cp -r static/ ../

cd ../
python2.7 manage.py makemigrations
python2.7 manage.py migrate
python2.7 manage.py collectstatic

../apache2/bin/restart