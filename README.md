# Installation

It is recommended to have Docker installed and to launch the project with it. However, there are options.

To launch the project with Docker, it is required:

- To create an .env file with the following variables:
1. PYTHONUNBUFFERED=1
2. SECRET_KEY=`<django_secret_key>`
3. API_URL=`<api_url>`
4. BOT_TOKEN=`<bot_token>`
5. IMAGES_LOCAL_DIRECTORY=`<images_local_directory>`

- To launch the docker compose file:
```
docker compose up -d
```

# Tests Creation

To create your own test (using the admin panel), it is required:

- To create a super user (if you didn't do this already), using commands:
  ```
  docker exec -it art_game bash
  ```
  ```
  python manage.py createsuperuser
  ```
- To enter the admin panel (add ":8000/admin" after the server address, if you didn't change anything).
- To add questions and answers. The question should have an image filename. The answers should have a reference to the question, an answer text, a correct/incorrect flag.
- To load images to the images project folder.

After launching the bot, you should see something like this:

![Alt Text](art_game.gif)
