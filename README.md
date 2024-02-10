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

## Running the Server

[Flask](https://flask.palletsprojects.com/en/3.0.x/) is used as the api server.

Start the server:

```
flask run
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

[^1]: This functionality is removable with [pinkyring](https://www.npmjs.com/package/pinkyring)
