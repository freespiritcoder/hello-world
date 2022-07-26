pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Pre-test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
