# Installation

It is recommended to have Docker installed and to launch the project with it. However, there are options.

To launch the project with Docker, it is required:

- To create an .env file with the following variables:
1. PYTHONUNBUFFERED=1
2. SECRET_KEY=`<django_secret_key>`
3. API_URL=`<api_url>`
4. BOT_TOKEN=`<bot_token>`
5. IMAGES_LOCAL_DIRECTORY=`<images_local_directory>`
- To launch the command that makes migrations:
```
python manage.py makemigrations
```
- And then:
```
python manage.py migrate
```
- Create a super user with the following command:
```
python manage.py createsuperuser
```
- Use the following command to launch the project with Docker:
```
docker compose up -d
```

# Tests Creation

Navigate to the admin panel that is located on the 8000 port (if you didn't change docker compose settings) of your server. It has an "/admin" endpoint.

To create a test, you should add the data into the questions and answers database models. In the questions model, there is an "image" field. You should add the filename of the image, that you would like to add to the test. Also, you should add the answers to a related question. The answer(s) that is (are) correct, should be marked as correct.

After launching the bot, you should see something like this:
![Alt Text](art_game.gif)