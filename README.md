# python-docker

# To deploy follow below instructions

1. git clone this repo

2. Make sure to install and configure Python:3

3. Install dependencies using command : pip install -r dependencies.txt .

4. run project : python server.py

5. Access application on : http://localhost:8080/ping

# To build docker image

    docker build -t <IMAGE_NAME>:<IMAGE_VERSION> <PATH_OF_Dockerfile>

# To run container from image

    docker run -d --name=<NAME_OF_CONTAINER_OPTIONAL> -p <HOST_PORT>:8080 <IMAGE_NAME>:<IMAGE_VERSION>

# Tag local image to docker hub repo

docker tag <local image name with version> <dockerhub repo name>

# To push docker image to docker

docker push <dockerhub repo name>

# To delete all local images forcefully

docker rmi -f $(docker images -a -q)
