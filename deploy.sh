pip install -r requirements.txt
python manage.py migrate
rm -f nohup.out
fuser -k 8000/tcp
nohup gunicorn -b 0.0.0.0:8000 emotorad.wsgi -k gevent &
