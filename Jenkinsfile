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
        stage('value set') {
            steps {
                script {
                    temp = sh (script: "python scripts/return.py", returnStdout: true)
                }
            }
        }
        stage('print custom') {
            steps {
                sh 'python scripts/argu.py temp'
            }
        }
    }
}
