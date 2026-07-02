pipeline {
    agent {
        label 'docker'
    }

    environment {
        IMAGE_NAME = "valeriomecocci/flask-app"
        DOCKER_CREDENTIALS = "dockerhub-credentials"
    }

    stages {

       stage('Build') {
            steps {
                script {
                    def image = docker.build("${IMAGE_NAME}:latest")
                    image.push()
                }
            }
        }

        stage('Login Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    """
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