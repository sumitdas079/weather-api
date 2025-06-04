# weather-api

Weather report app with automated deployment that publishes weather reports as artifacts that can be downloaded

### Set Secrets

Navigate to the repo Settings -> Security -> Security and Variables -> Actions

Add repository secrets

`DOCKER_USERNAME` AND `DOCKER_PASSWORD`

### Steps to run:

Build docker image

`docker build -t weather-api .`

Run application

`docker run -p 8000:80 weather-api`
