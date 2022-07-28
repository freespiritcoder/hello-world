pipeline {
    parameters {
        string(name: 'custom_var', defaultValue: '')
    }
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
                    env.custom_var = sh (script: "python scripts/return.py", returnStdout: true).trim()
                   # env.custom_var = temp
                }
            }
        }
        stage('print custom') {
            steps {
                echo "${env.custom_var}"
            }
        }
    }
}
