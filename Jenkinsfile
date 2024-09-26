pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'flask-crud-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git...'
                git branch: 'main', url: 'https://github.com/J95686/flaskjenkins.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Docker image...'
                script {
                    def app = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Test') {
            steps {
                echo 'Creating and activating virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    venv/bin/python -m unittest test.py
                '''
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    . venv/bin/activate
                    pip install pylint
                    pylint app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Docker image to staging environment...'
                sh '''
                    docker stop flask-crud-app-staging || true
                    docker rm flask-crud-app-staging || true
                    docker run -d -p 8081:5000 --name flask-crud-app-staging ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}
                '''
            }
        }

        stage('Release') {
            steps {
                echo 'Deploying Docker image to production environment...'
                sh '''
                    docker stop flask-crud-app-prod || true
                    docker rm flask-crud-app-prod || true
                    docker run --rm -d -p 80:5000 --name flask-crud-app-prod ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished with status: ' + currentBuild.currentResult
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
