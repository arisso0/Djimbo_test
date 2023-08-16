``` 
docker-compose up -d --build
docker-compose run django python manage.py migrate 
docker-compose run django python manage.py createsuperuser
docker-compose run django python manage.py loaddata data.json
```
