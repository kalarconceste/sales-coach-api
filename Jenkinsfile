pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE = 'sales-coach-api'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        // Replace with your actual DockerHub username
        DOCKER_USER = 'karenalarcon' 
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build and Test') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    dockerImage = docker.build("${env.DOCKER_USER}/${env.DOCKER_IMAGE}:${env.DOCKER_TAG}")
                    
                    echo 'Running Tests inside Container...'
                    dockerImage.inside {
                        sh 'pytest --junitxml=test-results.xml'
                    }
                }
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Trivy Scan') {
            steps {
                echo 'Scanning Docker Image for Vulnerabilities...'
                // sh "trivy image ${env.DOCKER_USER}/${env.DOCKER_IMAGE}:${env.DOCKER_TAG}"
                echo 'Trivy scan skipped for simulation (requires trivy installed)'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing Image to DockerHub...'
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }


}
