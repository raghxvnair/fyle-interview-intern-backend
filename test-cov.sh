# virtualenv env --python=python3.8
# source env/bin/activate
# pip install -r requirements.txt

export FLASK_APP=core/server.py
rm core/store.sqlite3 
flask db upgrade -d core/migrations/
pytest --cov
coverage html