pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        DOCKER_NAMESPACE = "madhudocker03"

        BACKEND_IMAGE = "${DOCKER_NAMESPACE}/backend"
        FRONTEND_IMAGE = "${DOCKER_NAMESPACE}/frontend"

        IMAGE_TAG = "1"
    }

    stages {

        stage('Checkout Source') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Kolipaka97/web_applications.git'
            }
        }

        stage('Build Docker Images') {
            steps {
                sh '''
                docker build -t ${BACKEND_IMAGE}:${IMAGE_TAG} backend
                docker build -t ${FRONTEND_IMAGE}:${IMAGE_TAG} frontend
                '''
            }
        }

        stage('Run Unit Tests (Backend)') {
            steps {
                sh '''
                docker run --rm ${BACKEND_IMAGE}:${IMAGE_TAG} pytest
                '''
            }
        }

        stage('Security Scan (Trivy)') {
            steps {
                sh '''
                trivy image --severity HIGH,CRITICAL ${BACKEND_IMAGE}:${IMAGE_TAG}
                trivy image --severity HIGH,CRITICAL ${FRONTEND_IMAGE}:${IMAGE_TAG}
                '''
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Images to Registry') {
            steps {
                sh '''
                docker push ${BACKEND_IMAGE}:${IMAGE_TAG}
                docker push ${FRONTEND_IMAGE}:${IMAGE_TAG}
                '''
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                export BACKEND_IMAGE=${BACKEND_IMAGE}:${IMAGE_TAG}
                export FRONTEND_IMAGE=${FRONTEND_IMAGE}:${IMAGE_TAG}

                docker compose down
                docker compose up -d
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                sleep 10
                curl -f http://localhost || exit 1
                '''
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
    }
}
