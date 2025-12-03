pipeline {
    agent any

    stages {
        
        stage('Checkout') {
            steps {
                echo "Branch: ${env.BRANCH_NAME}"
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Build') {
            when {
                branch 'main'
            }
            steps {
                echo "Building only on the main branch"
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                echo "Deploying only from main branch"
            }
        }
    }
}
