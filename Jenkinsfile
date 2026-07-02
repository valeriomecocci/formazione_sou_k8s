pipeline {
    agent {
        label 'docker'
    }

    environment {
        IMAGE_NAME = "valeriomecocci/flask-app"
    }

    stages {


        stage('Debug') {
            steps {
                sh 'printenv | sort'
            }
        }


        stage('Determine Docker Tag') {
            steps {
                script {

                    if (env.TAG_NAME) {

                        env.IMAGE_TAG = env.TAG_NAME

                    } else if (env.BRANCH_NAME == 'master') {

                        env.IMAGE_TAG = "latest"

                    } else if (env.BRANCH_NAME == 'develop') {

                        env.IMAGE_TAG = "develop-${env.GIT_COMMIT.take(7)}"

                    } else {

                        error("Branch non supportato")

                    }

                    echo "Docker tag: ${env.IMAGE_TAG}"
                }
            }
        }

        /*---- RIDONDANTE:questo stage Checkout se se usa la modalità SCM della pipeline---
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valeriomecocci/formazione_sou_k8s.git'
            }
        }
        -------------------------*/

        stage('Build') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Login Docker Hub') {
            steps {

                /*qui uso il jenkins binding plugin

                withCredentials prende delle credenziali salvate in Jenkins e le rende diponibili 
                come variabili d'ambiente temporaneamente: NON LE LEGGE, le recupera dal credential store
                di Jenkins. Finito questo blocco, le variabili al suo interno vengono eliminate

                usernamePassword è un oggetto fornito dal plugin che indica che le credenziali sono 
                formate da username + password
                */
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    //id delle credenziali, DockerHub in questo caso, aggiunte su jenkins

                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                    //in questo caso la passwd è il token di dockerhub
                )]) {
                    
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    //--password-stdin signifca che la password viene acquisita dall'input s
                    //standard, cioè dalla pipe
                }
            }
        }

        stage('Push') {
            steps {
                sh "docker push $IMAGE_NAME:$IMAGE_TAG"
            }
        }
    }
}