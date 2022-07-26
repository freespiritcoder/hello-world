pipeline {
    agent any
    stages {
        stage('Pre-test') {
            steps {
                sh 'python --version'
                sh 'pip install BeautifulSoup4==4.9.3.0'
                sh 'python scripts/pre_test.py'
            }
        }
    }
}
