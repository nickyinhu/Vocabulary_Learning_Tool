To install (use pip install):
Flask
peewee
PyMySQL
gunicorn
gevent

model generator:
python -m pwiz -e mysql -u 6400 -P -H $db_host vocabulary > models.py

To deploy:
sudo gunicorn -k gevent -w 4 -b 0.0.0.0:80 vocabulary:app &
