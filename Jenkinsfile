
pipeline {

    agent any

    stages {

        // C Application Pipeline

        stage('Check GCC') {
            steps {
                sh 'gcc --version'
            }
        }

        stage('Compile C') {
            steps {
                sh 'gcc -Wall -Wextra -Werror -o c_app main.c'
            }
        }

        stage('Run C Application') {
            steps {
                sh './c_app'
            }
        }

        stage('Test C Application') {
            steps {
                sh '''
                    output=$(./c_app)
                    echo "$output"
                    echo "$output" | grep -q "Addition: 30"
                    echo "C TEST PASSED"
                '''
            }
        }

        // Python Application Pipeline

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Python Application') {
            steps {
                sh 'python3 avinash.py'
            }
        }
    }

    // Common post-build actions

    post {

        success {
            echo 'C and Python applications completed successfully!'
        }

        failure {
            echo 'C or Python application pipeline failed!'
        }
    }
}

