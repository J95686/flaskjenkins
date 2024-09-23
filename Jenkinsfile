pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }
        stage('Build Docker image') {
            steps {
                script {
                    def app = docker.build("flask-crud-app")
                }
            }
        }
    }
}
