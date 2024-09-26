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

        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r workspace/flaskjenkins/requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running unit tests...'
                sh 'venv/bin/python -m unittest discover -s tests'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running code quality checks...'
                sh 'pylint app.py'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    def app = docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying Docker image to staging environment...'
                sh 'docker stop flask-crud-app-staging || true'
                sh 'docker rm flask-crud-app-staging || true'
                sh 'docker run -d -p 8081:5000 --name flask-crud-app-staging ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying Docker image to production environment...'
                sh 'docker stop flask-crud-app-prod || true'
                sh 'docker rm flask-crud-app-prod || true'
                sh 'docker run --rm -d -p 80:5000 --name flask-crud-app-prod ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring production environment...'
                // Add monitoring steps here
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
