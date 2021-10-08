# Bank Account
This is a test project with the idea to make a API that can manage an account with differents types of currencies

### Environment
For the project to run you need to install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)  
If you are in linux you may need to make this [configurations](https://docs.docker.com/engine/install/linux-postinstall/)

```bash
$ docker-compose up --build
```

Environment variable | Example value | Required | Default
--- | --- | --- | --- 
PYTHONDONTWRITEBYTECODE  | 1 | YES | 1
DJANGO_DEBUG  | True | YES | True
DATABASE_URL  | `postgres://USER:PASSWORD@HOST:PORT/NAME` | YES | 
POSTGRES_HOST  | HOST | YES | 
POSTGRES_PORT  | XXXX | YES | 
POSTGRES_DB  | DB_NAME | YES | 
POSTGRES_USER  | USER_NAME | YES | 
POSTGRES_PASSWORD  | PASSWORD | YES | 
