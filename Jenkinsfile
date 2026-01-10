pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = "docker.io"
        DOCKER_NAMESPACE = "madhudocker03"

        BACKEND_IMAGE = "${DOCKER_NAMESPACE}/backend"
        FRONTEND_IMAGE = "${DOCKER_NAMESPACE}/frontend"

        IMAGE_TAG = "1"
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {

        stage("Checkout Source") {
            steps {
                git branch: 'main', url: 'https://github.com/Kolipaka97/web_applications.git'
            }
        }

        stage("Build Docker Images") {
            steps {
                sh '''
                docker build -t $BACKEND_IMAGE:$IMAGE_TAG backend
                docker build -t $FRONTEND_IMAGE:$IMAGE_TAG frontend
                '''
            }
        }

        stage("Run Unit Tests (Backend)") {
            steps {
                sh '''
                docker run --rm $BACKEND_IMAGE:$IMAGE_TAG pytest
                '''
            }
        }

        stage("Security Scan (Trivy)") {
            steps {
                sh '''
                trivy image --severity HIGH,CRITICAL $BACKEND_IMAGE:$IMAGE_TAG
                trivy image --severity HIGH,CRITICAL $FRONTEND_IMAGE:$IMAGE_TAG
                '''
            }
        }

        stage("Docker Login") {
            steps {
                withCredentials([
                    string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_PASS')
                ]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u madhudocker03 --password-stdin
                    '''
                }
            }
        }

        stage("Push Images to Registry") {
            steps {
                sh '''
                docker push $BACKEND_IMAGE:$IMAGE_TAG
                docker push $FRONTEND_IMAGE:$IMAGE_TAG
                '''
            }
        }

       stage('Deploy to Staging') {
    steps {
        sh '''
          export BACKEND_IMAGE=madhudocker03/backend:1
          export FRONTEND_IMAGE=madhudocker03/frontend:1

          docker compose down -v
          docker compose up -d
        '''
    }
}

        stage('Run Database Migration') {
            steps {
                sh '''
                echo "Skipping migrate since backend already runs migrations"
                '''
            }
        }

          stage("Verify Deployment") {
            steps {
                sh '''
                sleep 10
                curl -f http://localhost:3000
                curl -f http://localhost:5000/employees || true
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment successful!"
        }
        failure {
            echo " Pipeline failed!"
        }
        cleanup {
            sh "docker system prune -f"
        }
    }
} 
