# Pyforge final project
1. Install Docker: https://www.docker.com/
2. Copy project files into specific directory
3. For building and start containers execute a command in terminal:
``docker-compose up -d --build``
4. Get information about compounds from API:
``docker-compose exec web python manage.py get_data``
5. Print database table content
``docker-compose exec web python manage.py print_data``
6. Truncate compounds table:
``docker-compose exec web python manage.py clear_compounds``
7. Stop docker containers:
``docker-compose stop``
8. Stop docker containers and remove them:
``docker-compose down``
