# aicovid

## Requirements

- [Python >= 3.7](https://www.python.org/)
- [Pipenv](https://github.com/pypa/pipenv)
- [PostgreSQL](https://www.postgresql.org/)

## Development

1. Clone repository: `git clone https://github.com/Joaquinecc/aicovid`
2. Install dependencies: `pipenv install`
3. Create a file called `secrets.json` in root directory
4. Insert the following lines into the file:
   ```
   {
     "db_name": "db_name",
     "db_user": "<POSTGRESQL_DB_USER>",
     "db_password": "<POSTGRESQL_DB_PASSWORD>",
     "db_host": "<POSTGRESQL_DB_HOST>",
     "db_port": "<POSTGRESQL_DB_PORT>,
     "secret_key": "<DJANGO_SECRET_KEY>"
   }
   ```
5. Activate virtualenv: `pipenv shell`
6. Run migrations: `python manage.py migrate`
7. Install `unaccent` extension on your PostgreSQL database:
   ```
   $ psql -d adsum
   <DB_NAME>=# create extension unaccent;
   ```
8. Create SuperUser: `python manage.py createsuperuser`
9. Run Development Server: `python manage.py runserver`
