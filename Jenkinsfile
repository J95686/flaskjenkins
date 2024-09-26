pipeline {
    agent any 

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create virtual environment
                    bat 'python -m venv venv'
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    bat '''
                    venv\\Scripts\\activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and run tests
                    bat '''
                    venv\\Scripts\\activate
                    python -m unittest test.py
                    '''
                }
            }
        }
        stage('Start Flask App') {
            steps {
                script {
                    // Activate the virtual environment and run the Flask app
                    bat '''
                    venv\\Scripts\\activate
                    start flask run --host=0.0.0.0
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
