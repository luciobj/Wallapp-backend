# Wall App - Backend

## Context

This is a API, made to be consumed for the same App in [frontend](https://github.com/luciobj/wallapp-frontend), built with `python3`, `django`, `django-rest-framework`, and `djangorestframework-simplejwt`.

By using two entities (`user` and `post-it`), thi API allows user registration/authentication, and the authenticated user to handle basic **CRUD** (create, read, update and delete) operations.

## Requirements

- python 3.8
- docker 20.10

## Installation

First, make sure python 3.8 and docker are installed, and updated on your computer.

```bash
python3 --version
docker --version
```

Then, clone this repository
```bash
git clone git@github.com:luciobj/Wallapp-backend.git
cd Wallapp-backend
```

Run the docker command to made the first build and start the server.

```bash
docker-compose up --build
```

From now on, when starting the server, you can omit the '--build', as it is only needed on the first run. Also, you can use the `docker-compose up -d` command to have the api and database up, and release your terminal for use.

```bash
docker-compose up -d
```

This project uses the sendgrid API for sending emails after registration. Therefore, before starting the server, it is important that you create a `.env` file containing the following variables:

```
SENDGRID_API_KEY = <your_key_here>
FROM_EMAIL = <your_sender_email>
```
## Unit Testing

You can run the tests created for this application by running the command
```bash
docker-compose exec web pytest
```
And you can check the test coverage by running
```bash
docker-compose exec web pytest --cov
```
## Usage

After starting the server, you can try all the functionalities of this API by using an 'API Client' such as `Insomnia` or `Postman`.

This API is designed to be used by this front-end application [here](https://github.com/luciobj/wallapp-frontend). So you can also consider installing and running it if you want to see how everything works together.
