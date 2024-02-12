# python-flask-template

## Environment

The environment is managed by [Mamba](https://github.com/mamba-org/mamba) which is a fast, cross-platform package manager for Python.
So, Mamba needs to be installed first.
If you are using WSL, this [WSL Setup project](https://github.com/CaseyHaralson/wsl-setup) can be used to help setup a Linux VM in Windows with all the prerequisites.

To create the environment with the necessary packages:

```
mamba env create -f environment.yml
```

Switch to the environment:

```
mamba activate python-flask-template
```

### Package Management

Install a new package: 

```
mamba install [package]
```

Update a package:

```
mamba update [package]
```

Export the new packages to the environment file:

```
mamba env export --from-history | grep -v '^prefix: ' > environment.yml
```

## Running the Server Locally

[Flask](https://flask.palletsprojects.com/en/3.0.x/) is used as the api server.

Start the server locally with live code reload:

```
flask --debug run
```

The server should now be running and you can hit the "Hello World" endpoint: http://127.0.0.1:5000/api/hello

## VSCode Intellisense

To get VSCode to pick up intellisense in python files, open the Command Palette (Ctrl + Shift + P), select "Python: Select Interpreter", and pick the "python-flask-template" mamba environment.

[//]: # (.pinkyring=DOCKER)

## Docker

[^1]

Build the docker image:

```
docker build -t python-flask-template:latest .
```

Run the docker image:

```
docker run -e PORT=5000 -p 5000:5000 --name python-flask-template -d python-flask-template
```

Stop and remove the container:

```
docker stop python-flask-template && docker rm python-flask-template
```

[//]: # (.pinkyring=DOCKER.end)

## Infrastructure

A [docker-compose.infra.yml](./devops/docker-compose.infra.yml) file has been added that can be used to add any docker services (databases, caches, etc) that are needed during development.

Start the infrastructure:

```
docker compose -f ./devops/docker-compose.infra.yml -p python-flask-template up -d
```

Stop the infrastructure:

```
docker compose -f ./devops/docker-compose.infra.yml -p python-flask-template down
```

[//]: # (.pinkyring=MONGO)

### Document DB

[^1]

Mongo has been added as the document database, and [pymongo](https://pymongo.readthedocs.io/en/stable/) has been added as the connector to Mongo.
[mongo-express](https://github.com/mongo-express/mongo-express) has also been added that runs with the infrastructure (user: admin, password: pass).

The configuration for the database is done in the [config.py file](./app/infrastructure/document_db/config.py).
The following environment variable configurations can be set (or these defaults can be used during development):

```
MONGO_USER      = mongo
MONGO_PASSWORD  = mongo
MONGO_HOST      = localhost
MONGO_PORT      = 27017
MONGO_DB        = db
```

To connect to the database and start using Mongo:

```
from app.infrastructure.document_db import document_db

_COLLECTION = "test"

// start using the connection
items = document_db[_COLLECTION].find()
```

Several example apis handling document listing, selection by id, creation, update, and deletion have been added in the [document api file.](./app/api/document.py)

[//]: # (.pinkyring=MONGO.end)

[^1]: This functionality is removable with [pinkyring](https://www.npmjs.com/package/pinkyring)
