FROM python:3.13

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["sh", "-c", "python manage.py makemigrations art_game && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]