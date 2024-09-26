pipeline {
    agent any 

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create virtual environment
                    sh 'python3 -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    sh '''
                    . venv/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    sh '''
                    . venv/bin/activate
                    python -m unittest test.py
                    '''
                }
            }
        }
        stage('Start Flask App') {
            steps {
                script {
                    // Activate the virtual environment and run the Flask app
                    sh '''
                    . venv/bin/activate
                    FLASK_APP=app.py flask run &
                    '''
                }
            }
        }
    }
    post {
        always {
            // Clean up the workspace
            cleanWs()
        }
    }
}
