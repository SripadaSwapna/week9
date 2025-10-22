pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image"
                bat "docker build -t erum_repo:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                // Use your Docker Hub credentials
                bat "docker login -u erumfaiz -p Erum@3005"
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub"
                bat "docker tag erum_repo:v1 erumfaiz/erum_repo:v1"
                bat "docker push erumfaiz/erum_repo:v1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying to Kubernetes"
                bat "kubectl apply -f deployment.yaml --validate=false"
                bat "kubectl apply -f service.yaml"
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
