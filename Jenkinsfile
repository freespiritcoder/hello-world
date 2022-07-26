pipeline {
    agent
    stages {
        stage('Pre-test') {
            steps {
                sh 'python --version'
                sh 'python scripts/pre_test.py'
            }
        }
    }
}
