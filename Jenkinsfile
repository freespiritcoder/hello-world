pipeline {
    agent any
    stages {
        stage('Pre-test') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install requests'
                sh 'python3 scripts/pre_test.py'
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
