pipeline {
    agent any

    environment {
        PYTHONUNBUFFERED = '1'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Setup Environment & Install Dependencies') {
            steps {
                echo 'Setting up Python virtual environment and installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pytest Tests') {
            steps {
                echo 'Running automated test suite with pytest...'
                sh '''
                    . venv/bin/activate
                    pytest -v --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'test-results.xml'
        }
        success {
            echo '=================================================='
            echo ' CI PIPELINE SUCCEEDED: All pytest checks passed! '
            echo '=================================================='
        }
        failure {
            echo '=================================================='
            echo ' CI PIPELINE FAILED: Please check the test logs. '
            echo '=================================================='
        }
    }
}
