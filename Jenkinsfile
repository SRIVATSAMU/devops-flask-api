pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Source code downloaded from GitHub'
            }
        }

        stage('Validate Project') {
            steps {
                sh '''
                    set -eu
                    test -f app/main.py
                    test -f app/requirements.txt
                    test -f docker/Dockerfile
                    test -f docker-compose.yml
                    test -f README.md
                    echo "All required project files are present!"
                '''
            }
        }
    }

    post {
        success {
            echo 'CI Pipeline completed successfully!'
        }
        failure {
            echo 'CI Pipeline failed. Check the logs.'
        }
    }
}
