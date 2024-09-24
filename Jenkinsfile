pipeline {
    agent any

    environment {
        // Define environment variables if needed
        DOCKER_IMAGE_NAME = 'flask-crud-app'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from Git...'
                git branch: 'main', url: 'https://github.com/your-username/your-repository.git'
            }
        }

        stage('Install dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Code Quality Analysis') {
            steps {
                echo 'Running code quality checks (this can be customized with tools like pylint or flake8)...'
                // Example: Run a linter or static code analyzer (if applicable)
                sh 'pylint your_python_files'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    echo 'Building Docker image...'
                    def app = docker.build("${DOCKER_IMAGE_NAME}")
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                echo 'Deploying Docker image to staging environment...'
                sh 'docker stop flask-crud-app-staging || true'
                sh 'docker rm flask-crud-app-staging || true'
                sh 'docker run -d -p 8081:5000 --name flask-crud-app-staging flask-crud-app'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Deploying Docker image to production environment...'
                sh 'docker stop flask-crud-app-prod || true'
                sh 'docker rm flask-crud-app-prod || true'
                sh 'docker run --rm -d -p 80:5000 --name flask-crud-app-prod flask-crud-app'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Monitoring production environment...'
                // Add any monitoring steps here (e.g., integration with New Relic, Prometheus, etc.)
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
