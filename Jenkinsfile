pipeline {
    agent any

    environment {
        dockerImage = ""
        registry = "tyagianant98/python-project"
        dockerHubCreds = "dockerhub_anant"
        EXAMPLE_CREDS = credentials('dockerhub_anant')
    }

    stages {
        stage('Build docker image') {
            steps {
                sh 'rm -rf python-docker'
                sh 'git clone https://github.com/tyagianant98/python-docker.git/'
                sh 'cd python-docker'
                sh 'ls -lrth'
                sh 'ls -lrth ./python-docker'
                sh "docker build -t python-docker:${BUILD_ID} ./python-docker/app"
            }

            post {
                success {
                    sh "echo 'build success'"
                }
            }
        }

        stage('Publish image to docker registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_anant', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh('docker login --username=tyagianant98 --password="PWD"')
                    sh "docker tag python-docker:${BUILD_ID} tyagianant98/python-project:${BUILD_ID}"
                    sh "docker push tyagianant98/python-project:${BUILD_ID}"
                }
            }

            post {
                success {
                    sh "echo 'docker image published successfully'"
                }
            }
        }
    }
}
