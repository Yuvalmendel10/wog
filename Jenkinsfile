pipeline {
    agent any

    environment {
        DOCKER_COMPOSE_VERSION = '1.26.0'
        DOCKER_IMAGE_NAME = 'yuvalmendel10/wog:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Download and install Docker Compose
                script {
                    sh "curl -L https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose"
                    sh "chmod +x /usr/local/bin/docker-compose"
                }
                // Build the Docker image using docker-compose
                script {
                    sh "docker-compose build"
                }
            }
        }

        stage('Run') {
            steps {
                // Run the Docker container using docker-compose
                script {
                    sh "docker-compose up -d"
                }
            }
        }

        stage('Test') {
            steps {
                // Run Selenium tests using e2e.py
                script {
                    sh 'python e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                // Stop and push the Docker image
                script {
                    sh "docker-compose down"
                    sh "docker-compose push"
                }
            }
        }
    }
}
