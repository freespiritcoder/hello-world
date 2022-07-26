pipeline {
    agent any
    stages {
        stage('Pre-test') {
            steps {
                sh 'python --version'
                sh 'pip install bs4'
                sh 'python scripts/pre_test.py'
            }
        }
    }
}
