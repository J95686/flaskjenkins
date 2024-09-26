pipeline {
    agent any 

    environment {
        VENV_DIR = 'venv' // Directory for virtual environment
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Create a virtual environment
                    sh "python3 -m venv ${VENV_DIR}"

                    // Activate virtual environment and install dependencies
                    sh """
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                    """
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests using unittest
                    sh """
                    . ${VENV_DIR}/bin/activate
                    python test.py
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Here you can add deployment commands.
                    echo 'Deploying the application...'
                }
            }
        }
        
        stage('Release') {
            steps {
                script {
                    // Add release steps here (e.g., notifying users, versioning, etc.)
                    echo 'Releasing the application...'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Clean up virtual environment if necessary
            sh "rm -rf ${VENV_DIR}"
        }
    }
}
