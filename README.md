# Bank Account
This is a test project with the idea to make a API that can manage an account with differents types of currencies.  
  
This project is develop with [Django](https://www.djangoproject.com/) and [DjangoREST](https://www.django-rest-framework.org/).  
The project have one simply Users app, that allows you to verify the account by [JWT](https://jwt.io/), and use Token authentication for the API comunications.  
For the emulation of the bank_account the app have 3 models:
- Account
- Currency
- Tansfers  

You could interact with each of this models by the differents endpoints. 
You can see the examples on the tests. 


### Environment
For the project to run you need to install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)  
If you are in linux you may need to make this [configurations](https://docs.docker.com/engine/install/linux-postinstall/)

```bash
$ docker-compose up --build
```

Environment variable | Example value | Required | Default
--- | --- | --- | --- 
PYTHONDONTWRITEBYTECODE  | 1 | YES | 1
DJANGO_DEBUG  | True | YES | 
DJANGO_HOST  | True | YES | 
DJANGO_DEBUG  | True | YES | True
DATABASE_URL  | `postgres://USER:PASSWORD@HOST:PORT/NAME` | YES | 
POSTGRES_HOST  | HOST | YES | 
POSTGRES_PORT  | XXXX | YES | 
POSTGRES_DB  | DB_NAME | YES | 
POSTGRES_USER  | USER_NAME | YES | 
POSTGRES_PASSWORD  | PASSWORD | YES | 


### Tests
This project have all the endpoint tested, to run the test you only need to use this command: 
```bash
$ docker-compose run --rm django pytest -s -v
```
