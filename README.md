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

# To delete all the containers forcefully

    docker rm -vf $(docker ps -a -q)

# Enable dashboard in Kubernetes

    microk8s enable dashboard

    token=$(microk8s kubectl -n kube-system get secret | grep default-token | cut -d " " -f1)

    microk8s kubectl -n kube-system describe secret $token

    microk8s kubectl port-forward -n kube-system service/kubernetes-dashboard 10443:443

    https://127.0.0.1:10443

# Create deployment

    kubectl create deployment tyagianant --image=tyagianant98/python-project:v19

# Update replica set

    kubectl scale --replicas=2 deployments/tyagianant

# Expose deployment as service

    kubectl expose deployment tyagianant --port=8080 --target-port=8080

# Delete a deployment

    kubectl delete deployment tyagianant

    kubectl delete deployments/tyagianant

# For apiversion:

    kubectl api-resources | grep deployment

# Create service and deployment by yml file:

    kubectl create -f <yml file name>

# Update after changes by yml file:

    kubectl apply -f <yml file name>
