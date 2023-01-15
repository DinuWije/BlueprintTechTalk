# Blueprint Tech 101 - A mini tech talk
## Part 1: Git
### Steps:
- Go to github
- Git pull the project
    - SSH vs HTTP: two different ways of authenticating. SSH is usually quicker, but you have to set it up.
    - https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
- Common git commands:
    - git pull
    - git checkout [-b branchname]
    - git add [filename / . ]
    - git commit [-m message]
    - git push
- Try pulling this repo, running it, and then making a branch and a new commit
    - `python hello.py`

## Part 2: Postman
- Download Postman
- Try hitting the following api with a GET request
    - https://api.agify.io?name=dinu
- Now try starting up the app.py application in this repo
    - run `pip install -r requirements.txt` to install dependencies
    - `export FLASK_APP=app.py` to tell your terminal what the flask app is called
    - `flask --app app.py --debug run` to start the flask app
    - try hitting `localhost:5000/` in Postman to see what happens. What about in your browser?
    - try passing in query params `user` and `term`

## Part 3: Docker
- Download Docker
- Steps to run the container:
    - build image `docker build --tag python-docker .`
    - view images with `docker images`
    - `docker run python-docker` to run the container
    - `docker run -d -p 5000:5000 python-docker` to run the container and port forward
- Other useful commands:
    - view running containers: `docker ps`
    - stop a container: `docker stop <container_id>` 
    - free up unused resources: `docker container prune`
