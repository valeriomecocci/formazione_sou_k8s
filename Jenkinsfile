pipeline {
    agent {
        label 'docker'
    }

    environment {
        IMAGE_NAME = "valeriomecocci/flask-app"
    }

    stages {

        // Determina il tag dell'immagine Docker in base al branch Git
        stage('Determine Docker Tag') {
            steps {
                script {

                    if (env.GIT_BRANCH == 'origin/main') {

                        env.IMAGE_TAG = "latest"

                    } else if (env.GIT_BRANCH == 'origin/develop') {

                        env.IMAGE_TAG = "develop-${env.GIT_COMMIT.take(7)}"

                    } else {

                        error("Branch non supportato")

                    }

                    echo "Tag Docker: ${env.IMAGE_TAG}"
                }
            }
        }

        /*---- RIDONDANTE: questo stage Checkout non serve se si usa
              la modalità "Pipeline script from SCM"

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/valeriomecocci/formazione_sou_k8s.git'
            }
        }

        --------------------------------------------------------------*/

        stage('Build') {
            steps {
                sh "docker build -t $IMAGE_NAME:$IMAGE_TAG ."
            }
        }

        stage('Login Docker Hub') {
            steps {

                /*
                 * withCredentials è uno step del Jenkins Credentials Binding Plugin.
                 * Recupera le credenziali salvate nel Credential Store di Jenkins
                 * e le rende disponibili come variabili d'ambiente temporanee.
                 *
                 * usernamePassword indica che la credenziale è composta
                 * da username e password (in questo caso il token Docker Hub).
                 */

                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',

                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    /*
                     * Docker legge il token dallo standard input (stdin),
                     * che riceve il valore tramite la pipe dal comando echo.
                     */

                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    '''
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