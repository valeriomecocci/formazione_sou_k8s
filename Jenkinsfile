pipeline {
    agent {
        label 'docker'
    }

    environment {
        IMAGE_NAME = "valeriomecocci/flask-app"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valeriomecocci/formazione_sou_k8s.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME:latest ."
                }
            }
        }

        stage('Login Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS) {
                        echo "Logged into Docker Hub"
                    }
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', DOCKER_CREDENTIALS) {
                        sh "docker push $IMAGE_NAME:latest"
                    }
                }
            }
        }
    }
}
