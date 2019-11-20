# RAVEN project

## Getting started

### Prerequisites
- `Docker` version 19.03.1, build 74b1e89 (or higher)
- `docker-compose` version 1.22.0, build f46880fe (or higher)

### Startup

1. Inside the project folder create a hidden environment file called `.env` 
with <a href="#env-file">these contents</a>
1. Inside the project folder run in the console `docker-compose up`
1. Check if the `api-server` & `db-server` are up: `docker ps`. 
You should see the __STATUS__ as _Up X minutes_
1. Create a superuser from the console. This can only be done via console.
`docker-compose exec api-server python3 manage.py createsuperuser`
1. Access the admin interface at `localhost:8000/admin`

### ENV file
```text
# generic
PYTHONUNBUFFERED=true

# for postgres
POSTGRES_DB=some_db_name
POSTGRES_USER=some_db_user
POSTGRES_PASSWORD=some_hard_password
```
### CLI
1. To access the DB: `docker-compose exec api-server python3 manage.py dbshell`
1. To run all the unit tests: `docker-compose exec api-server python3 manage.py test`
