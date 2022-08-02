pipeline {
    agent any
    stages {
        stage('Pre-test') {
            steps {
                sh 'python --version'
                sh 'python scripts/pre_test.py'
            }
        }
        stage('value set') {
            steps {
                script {
                    temp = sh (script: "python scripts/return.py", returnStdout: true).trim()
                }
            }
        }
        stage('print custom') {
            steps {
                sh 'python scripts/argu.py ' + temp
            }
        }
    }
}
