pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'sales-coach-api'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_USER = 'karenalarcon'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                bat "docker build -t %DOCKER_USER%/%DOCKER_IMAGE%:%DOCKER_TAG% ."
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running Tests inside Container...'
                // Mount workspace to capture test results. 
                // We use %WORKSPACE% to map the current Jenkins directory to /app in the container.
                bat "docker run --rm -v \"%WORKSPACE%:/app\" %DOCKER_USER%/%DOCKER_IMAGE%:%DOCKER_TAG% pytest --junitxml=/app/test-results.xml"
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Skipping SonarQube (Simulation)'
            }
        }

        stage('Trivy Scan') {
            steps {
                echo 'Skipping Trivy Scan (Simulation)'
            }
        }

        stage('Push to DockerHub') {
            steps {
                echo 'Pushing to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER_VAR')]) {
                    bat "docker login -u %DOCKER_USER_VAR% -p %DOCKER_PASS%"
                    bat "docker push %DOCKER_USER%/%DOCKER_IMAGE%:%DOCKER_TAG%"
                    // Tag and push latest
                    bat "docker tag %DOCKER_USER%/%DOCKER_IMAGE%:%DOCKER_TAG% %DOCKER_USER%/%DOCKER_IMAGE%:latest"
                    bat "docker push %DOCKER_USER%/%DOCKER_IMAGE%:latest"
                }
            }
        }
    }
    
    post {
        always {
            // Cleanup docker images to save space (optional, safe to fail)
            bat "docker rmi %DOCKER_USER%/%DOCKER_IMAGE%:%DOCKER_TAG% || exit 0"
        }
    }
}
