pipeline {
    agent any

    environment {
        APP_NAME = "flask-app"
        IMAGE_TAG = "local-${env.BUILD_NUMBER}"
        IMAGE_NAME = "${APP_NAME}:${IMAGE_TAG}"
        DEPLOYMENT_NAME = "flask-app-deployment"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo "Fetching source code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${IMAGE_NAME}"
                    bat "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

stage('Load Image into Kubernetes') {
    steps {
        script {
            echo "Loading Docker image into Minikube..."
            bat "minikube image load ${IMAGE_NAME}"
        }
    }
}


        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Deploying ${IMAGE_NAME} to Kubernetes..."
                    bat """
                    kubectl set image deployment/${DEPLOYMENT_NAME} ${APP_NAME}=${IMAGE_NAME} --record || (
                        kubectl apply -f k8s\\deployment.yaml &&
                        kubectl apply -f k8s\\service.yaml
                    )
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    bat """
                    kubectl rollout status deployment/${DEPLOYMENT_NAME} --timeout=120s
                    kubectl get pods -l app=${APP_NAME}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! Application is live."
            bat "kubectl get svc flask-app-service"
        }
        failure {
            echo "❌ Deployment failed. Check logs above."
        }
    }
}
