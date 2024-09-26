pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'flask-crud-app'
        DOCKER_REGISTRY = 'your-docker-registry' // Optional: Specify your Docker registry
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                sh '''
                    # Create and activate the virtual environment
                    python3 -m venv venv
                    . venv/bin/activate

                    # Install dependencies
                    pip install -r requirements.txt

                    # Build the Docker image
                    docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} .
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    venv/bin/python -m unittest discover -s tests
                '''
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running code quality checks...'
                sh '''
                    . venv/bin/activate
                    venv/bin/pylint app.py
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
                echo 'Releasing the application...'
                sh '''
                    echo 'Deploying to production...'
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
