# omdb-movies

OMDB movies list.

## Getting Started

### Prerequisites

- Python (version 3.11)
- Django (version 5.0.2)

### Installation

1. Clone the repository:

```sh
git clone https://github.com/zozulia-developer/omdb-movies
cd omdb-movies
```

2. Create a new virtual environment with pipenv and activate the virtual environment:
```sh
pipenv install
pipenv shell
```

3. Run Django management commands and start the development server
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser

python manage.py runserver
```

## Usage of fetching data from OMDB

To fetch movie data from the OMDB API and save it to the database, you can use the `fetch_movie` management command.

Run the following command, replacing `<movie title>` with the title of the movie you want to fetch:

```sh
python manage.py fetch_movie <movie title>
```

## Swagger API Documentation

The API is documented using Swagger. You can access the API documentation by running the development server and visiting the Swagger UI endpoint in your browser:

- Local server: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Production server: [https://yourdomain.com/swagger/](https://yourdomain.com/swagger/)

The Swagger UI provides interactive documentation for the API endpoints, allowing you to explore and test the API easily.

## Authentication with JWT Tokens

The API uses JSON Web Tokens (JWT) for authentication. To authenticate requests to protected endpoints, you need to include a JWT token in the Authorization header of your requests.

To obtain a JWT token, you can use the `obtain_jwt_token` endpoint with your username and password. Here's an example of how to obtain a token using cURL:

```sh
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email": "your_email", "password": "your_password"}'
```
1. Copy the JWT token from the response.
2. In the Swagger UI, click on the "Authorize" button in the top right corner.
3. Enter `Bearer <your_jwt_token_here>` in the "Value" field and click "Authorize".
4. Replace `<your_jwt_token_here>` with the JWT token obtained from the token endpoint.
5. You can now access and test authenticated endpoints in Swagger by sending requests with the JWT token in the Authorization header.
