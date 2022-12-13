# LEM
Social media for book lovers, similar to Goodreads.

# Getting started
## Installing EditorConfig
To maintain consistent coding styles we use [EditorConfig](https://editorconfig.org/). The installation process is different depending on your editor:
* PyCharm has support for EditorConfig out of the box
* VSCode [needs a plugin](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
* If you use another editor reference to: https://editorconfig.org/#pre-installed or https://editorconfig.org/#download
## Installing Poetry
LEM is using [Poetry](https://python-poetry.org/) as a package manager. Check out [its documentation](https://python-poetry.org/docs/#installation) to learn how to install it. If you don't know what to do, we recommend following the installation steps with the official installer.

After the installation process, ensure Poetry is properly installed with 
```
poetry --version
```

We are also using the official export plugin for Poetry. You can install it with
```
poetry self add poetry-plugin-export
```

## Installing Docker
To install Docker head over to [the official documentation](https://docs.docker.com/get-docker/) and find instructions for your Operating System. With Docker Desktop you can start Docker conveneniently from the tray.
Make sure Docker is up and running:
```
docker --version
```

## Getting your hands on the project
Clone the repository (make sure you've got git installed):
```
git clone https://github.com/LemCommunity/lem.git
cd lem
```
Install the dependencies (Poetry will create a virtual environment automatically for you)
```
poetry install --with dev
```
If you want to enter the virtual environment run:
```
poetry shell
```

Build images and start containers. Don't worry if on the first run it takes a lot of time. Docker has to download a lot of data, but it will store it in cache for later retrieval.
```
docker-compose up --build -d
```
The `-d` flag runs the containers in the background so you can fire other commands from the same terminal.

If everything went smoothly without errors the application should now be running.
You can access it on
```
http://localhost:8000/
```
If you see the 404 Django page then everything is correct.

It might be useful to create a super user so you can access the Django Admin panel.
```
docker-compose run python manage.py createsuperuser
```

## Docker Cheat Sheet
See logs for a particular service:
```
docker-compose logs <SERVICE_NAME>
e.g.
docker-compose logs django
```



