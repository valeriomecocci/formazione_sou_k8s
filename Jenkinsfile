pipeline {
    agent {
        label 'docker'
    }

    environment {
        IMAGE_NAME = "valeriomecocci/flask-app"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valeriomecocci/formazione_sou_k8s.git'
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t $IMAGE_NAME:latest ."
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

        stage('Push') {
            steps {
                sh "docker push $IMAGE_NAME:latest"
            }
        }
    }
}