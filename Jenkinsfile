
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
                    test -f tests/test_api.py
                    echo "All required project files are present!"
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r app/requirements.txt
                    .venv/bin/python -m pip install pytest
                '''
            }
        }

        stage('Run Python Tests') {
            steps {
                sh '''
                    .venv/bin/python -m pytest -v
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
