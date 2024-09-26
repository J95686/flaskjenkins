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
                    . venv/Scripts/activate
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
                    . venv/Scripts/activate
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
                    . venv/Scripts/activate
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
